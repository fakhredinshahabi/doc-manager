import pathlib
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8",
        extra="ignore")

    app_name: str = "مدیر اسناد"
    upload_dir: str = "uploads"
    max_upload_bytes: int = 1_000_000
    session_max_age: int = 3600
    api_key: str = "dev-key-change-me"       # در .env عوضش کن
    cors_origins: list[str] = ["http://localhost:4200"]
    rate_limit_per_minute: int = 60


@lru_cache
def get_settings() -> Settings:
    return Settings()