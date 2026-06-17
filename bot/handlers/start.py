"""
Хэндлер команды /start.
Отправляет приветственное сообщение с инлайн-клавиатурой.
"""
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart

from bot.config import get_settings

router = Router()

# Текст приветствия (Markdown формат)
WELCOME_TEXT = """
🎉 *Добро пожаловать в {name}!*

Мы — площадка для лучших вечеринок, концертов и мероприятий.

Здесь вы можете:
• 📅 Смотреть афишу мероприятий
• 📞 Быстро связаться с администратором
• 🎫 Покупать билеты
• 💳 Управлять депозитом
• 🎁 Получать эксклюзивные акции

Выберите действие:
"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик /start — показывает главное меню."""
    settings = get_settings()

    # Инлайн-клавиатура главного меню (3 ряда по 2 кнопки)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📅 Афиша", callback_data="events"),
            InlineKeyboardButton(text="📞 Связаться", callback_data="contacts"),
        ],
        [
            InlineKeyboardButton(text="🎫 Билеты", callback_data="tickets"),
            InlineKeyboardButton(text="💳 Депозит", callback_data="deposit"),
        ],
        [
            InlineKeyboardButton(text="🎁 Акции", callback_data="promos"),
            InlineKeyboardButton(text="👤 Мой профиль", callback_data="profile"),
        ],
    ])

    await message.answer(
        WELCOME_TEXT.format(name="Venue Club"),
        reply_markup=kb,
        parse_mode="Markdown",
    )
