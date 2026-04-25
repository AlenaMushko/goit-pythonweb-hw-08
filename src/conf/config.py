import os

def _normalize_db_url(url: str) -> str:
    return url.replace("sqlite://", "sqlite+aiosqlite://", 1)


class Config:
    DB_URL = _normalize_db_url(
        os.getenv(
            "DATABASE_URL",
            "postgresql+asyncpg://hw_6_user:hw_6_password@127.0.0.1:5432/hw08",
        )
    )
    APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
    APP_PORT = int(os.getenv("APP_PORT", "8000"))


config = Config()