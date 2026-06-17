"""
Middleware для работы с БД.
Прокидывает user_id в контекст обработчика.
"""
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message


class DatabaseMiddleware(BaseMiddleware):
    """Базовый middleware — извлекает user_id из сообщения."""

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        # Передаём user_id дальше в обработчик
        data["user_id"] = event.from_user.id if event.from_user else None
        return await handler(event, data)
