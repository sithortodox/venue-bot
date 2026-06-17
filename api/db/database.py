"""
Настройка подключения к PostgreSQL.
AsyncEngine и сессии для асинхронной работы с SQLAlchemy.
"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from bot.config import get_settings

settings = get_settings()

# Асинхронный движок PostgreSQL
engine = create_async_engine(settings.database_url, echo=True)

# Фабрика асинхронных сессий
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Базовый класс для всех SQLAlchemy моделей."""
    pass


async def get_db():
    """Dependency для FastAPI — выдаёт сессию БД на запрос."""
    async with async_session() as session:
        yield session
