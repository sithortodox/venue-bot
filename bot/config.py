"""
Конфигурация приложения.
Загружает настройки из переменных окружения (.env файл).
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Основные настройки бота, БД и API."""
    bot_token: str = ""                          # Токен Telegram-бота
    admin_telegram_id: int = 0                   # Telegram ID администратора
    database_url: str = "postgresql+asyncpg://venue:venue_secret@db:5432/venue_db"
    redis_url: str = "redis://redis:6379/0"
    secret_key: str = "change-me"                # Секретный ключ для подписей
    mini_app_url: str = "http://localhost:3000"  # URL веб-приложения
    api_url: str = "http://api:8000"             # URL бэкенда

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """Кэширует настройки — читает .env только один раз."""
    return Settings()
