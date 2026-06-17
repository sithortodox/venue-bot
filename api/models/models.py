"""
SQLAlchemy модели (таблицы БД).
Определяют структуру: пользователи, мероприятия, бронирования.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.sql import func

from api.db.database import Base


class User(Base):
    """Пользователь — привязан к Telegram ID."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer, unique=True, nullable=False)  # Telegram ID пользователя
    username = Column(String(255))       # @username в Telegram
    first_name = Column(String(255))     # Имя из Telegram
    last_name = Column(String(255))      # Фамилия из Telegram
    phone = Column(String(20))           # Телефон (запрашивается при бронировании)
    is_admin = Column(Boolean, default=False)  # Является ли администратором
    deposit_balance = Column(Float, default=0)  # Баланс депозита
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Event(Base):
    """Мероприятие — афиша клуба."""
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)  # Название мероприятия
    description = Column(Text)                    # Описание
    date = Column(DateTime(timezone=True), nullable=False)  # Дата и время
    venue = Column(String(255))                   # Зона площадки (Main, VIP, Terrace)
    price = Column(String(100))                   # Строка с ценой ("от 1500₽")
    cover_image = Column(String(1000))            # URL обложки
    is_active = Column(Boolean, default=True)     # Видимо ли в афише
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Booking(Base):
    """Бронирование стола — заявка от пользователя."""
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.telegram_id"))  # Ссылка на пользователя
    event_name = Column(String(500))    # Название мероприятия
    name = Column(String(255))          # Имя гостя
    phone = Column(String(20))          # Телефон гостя
    guest_count = Column(Integer)       # Количество гостей
    status = Column(String(20), default="pending")  # Статус: pending/confirmed/cancelled
    notes = Column(Text)                # Примечания
    created_at = Column(DateTime(timezone=True), server_default=func.now())
