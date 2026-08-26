import secrets
from datetime import UTC, datetime, timedelta

from fastapi import APIRouter, HTTPException, Request, Response, status
from pwdlib import PasswordHash
from sqlalchemy import delete, select

from app.config import get_settings
from app.dependencies import AdminAccess, DbSession, digest
from app.models import AdminSession, User
from app.schemas import LoginRequest, UserRead

router = APIRouter()
password_hash = PasswordHash.recommended()


@router.post("/login", response_model=UserRead)
def login(payload: LoginRequest, response: Response, db: DbSession) -> User:
    user = db.scalar(select(User).where(User.email == payload.email.lower()))
    if not user or not user.active or not password_hash.verify(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo o contraseña incorrectos")

    settings = get_settings()
    session_token = secrets.token_urlsafe(48)
    csrf_token = secrets.token_urlsafe(32)
    expires_at = datetime.now(UTC) + timedelta(days=settings.session_days)
    db.execute(delete(AdminSession).where(AdminSession.expires_at < datetime.now(UTC)))
    db.add(AdminSession(token_hash=digest(session_token), csrf_hash=digest(csrf_token), user=user, expires_at=expires_at))
    db.commit()

    secure = settings.environment == "production"
    max_age = settings.session_days * 86400
    response.set_cookie("solidify_session", session_token, max_age=max_age, httponly=True, secure=secure, samesite="strict", path="/")
    response.set_cookie("solidify_csrf", csrf_token, max_age=max_age, httponly=False, secure=secure, samesite="strict", path="/")
    return user


@router.get("/me", response_model=UserRead)
def me(user: AdminAccess) -> User:
    return user


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(request: Request, response: Response, _: AdminAccess, db: DbSession) -> Response:
    token = request.cookies.get("solidify_session")
    if token:
        db.execute(delete(AdminSession).where(AdminSession.token_hash == digest(token)))
        db.commit()
    response.delete_cookie("solidify_session", path="/")
    response.delete_cookie("solidify_csrf", path="/")
    response.status_code = status.HTTP_204_NO_CONTENT
    return response

