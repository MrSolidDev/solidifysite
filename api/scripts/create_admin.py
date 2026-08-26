from sqlalchemy import select
from pwdlib import PasswordHash

from app.config import get_settings
from app.database import SessionLocal
from app.models import User


def run() -> None:
    settings = get_settings()
    email = settings.admin_email.lower()
    password = settings.admin_password.get_secret_value()
    hasher = PasswordHash.recommended()
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.email == email))
        if user:
            user.password_hash = hasher.hash(password)
            user.active = True
            action = "updated"
        else:
            db.add(User(email=email, password_hash=hasher.hash(password), active=True))
            action = "created"
        db.commit()
    print(f"Admin {action}: {email}")


if __name__ == "__main__":
    run()
