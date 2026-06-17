"""
Точка входа Telegram-бота.
Инициализирует бота, диспетчер, подключает роутеры и запускает polling.
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import get_settings
from bot.handlers import start, events, booking, contacts, profile
from bot.middlewares import db

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Главная функция — запуск бота."""
    settings = get_settings()

    # Инициализация бота и диспетчера
    bot = Bot(token=settings.bot_token)
    storage = MemoryStorage()  # Хранилище FSM (в памяти, для демо)
    dp = Dispatcher(storage=storage)

    # Подключение роутеров (обработчиков команд)
    dp.include_router(start.router)       # /start, главное меню
    dp.include_router(events.router)      # Афиша мероприятий
    dp.include_router(booking.router)     # Бронирование (FSM)
    dp.include_router(contacts.router)    # Контакты администратора
    dp.include_router(profile.router)     # Профиль + заглушки разделов

    # Подключение middleware (БД)
    dp.update.middleware(db.DatabaseMiddleware())

    logger.info("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
