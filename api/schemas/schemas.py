"""
Pydantic схемы — валидация данных для API запросов и ответов.
Create — для входящих данных, Response — для исходящих.
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# === Мероприятия ===

class EventCreate(BaseModel):
    """Схема создания мероприятия (входящий запрос)."""
    title: str
    description: Optional[str] = None
    date: datetime
    venue: Optional[str] = None
    price: Optional[str] = None
    cover_image: Optional[str] = None


class EventResponse(BaseModel):
    """Схема ответа с данными мероприятия."""
    id: int
    title: str
    description: Optional[str]
    date: datetime
    venue: Optional[str]
    price: Optional[str]
    cover_image: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True  # Совместимость с SQLAlchemy моделями


# === Бронирования ===

class BookingCreate(BaseModel):
    """Схема создания бронирования (из Telegram-бота)."""
    user_id: int
    event_name: str
    name: str
    phone: str
    guest_count: int
    notes: Optional[str] = None


class BookingResponse(BaseModel):
    """Схема ответа с данными бронирования."""
    id: int
    user_id: int
    event_name: str
    name: str
    phone: str
    guest_count: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# === Пользователи ===

class UserResponse(BaseModel):
    """Схема ответа с данными пользователя."""
    id: int
    telegram_id: int
    username: Optional[str]
    first_name: Optional[str]
    phone: Optional[str]
    deposit_balance: float

    class Config:
        from_attributes = True
