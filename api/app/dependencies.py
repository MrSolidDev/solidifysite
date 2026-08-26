import hashlib
import secrets
from datetime import UTC, datetime
from typing import Annotated

from fastapi import Cookie, Depends, Header, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import AdminSession, User

DbSession = Annotated[Session, Depends(get_db)]


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def require_admin(
    request: Request,
    db: DbSession,
    solidify_session: Annotated[str | None, Cookie()] = None,
    x_csrf_token: Annotated[str | None, Header()] = None,
) -> User:
    if not solidify_session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    session = db.scalar(
        select(AdminSession)
        .where(AdminSession.token_hash == digest(solidify_session))
        .options(joinedload(AdminSession.user))
    )
    now = datetime.now(UTC)
    if not session or session.expires_at.replace(tzinfo=session.expires_at.tzinfo or UTC) <= now or not session.user.active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired")
    if request.method not in {"GET", "HEAD", "OPTIONS"}:
        if not x_csrf_token or not secrets.compare_digest(digest(x_csrf_token), session.csrf_hash):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid CSRF token")
    return session.user


AdminAccess = Annotated[User, Depends(require_admin)]

