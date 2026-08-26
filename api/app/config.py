from functools import lru_cache

from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Solidify Content API"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://solidify:solidify@localhost:5432/solidify"
    admin_email: str = "admin@solidify.local"
    admin_password: SecretStr = SecretStr("change-me-locally")
    session_days: int = 7
    upload_directory: str = "/app/uploads"
    max_upload_bytes: int = 8 * 1024 * 1024
    allowed_origins: list[str] = ["http://localhost:5173"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SOLIDIFY_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @model_validator(mode="after")
    def reject_default_production_secret(self) -> "Settings":
        if self.environment == "production" and self.admin_password.get_secret_value() == "change-me-locally":
            raise ValueError("SOLIDIFY_ADMIN_PASSWORD must be changed in production")
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
