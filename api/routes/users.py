"""
API роутер — пользователи.
Получение профиля по Telegram ID (авторегистрация при первом обращении).
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.db.database import get_db
from api.models.models import User
from api.schemas.schemas import UserResponse

router = APIRouter()


@router.get("/{telegram_id}", response_model=UserResponse)
async def get_user(telegram_id: int, db: AsyncSession = Depends(get_db)):
    """
    GET /api/users/{telegram_id} — получить профиль пользователя.
    Если пользователя нет — создаёт нового (авторегистрация).
    """
    result = await db.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()

    # Авто-создание при первом обращении
    if not user:
        user = User(telegram_id=telegram_id)
        db.add(user)
        await db.commit()
        await db.refresh(user)

    return user
