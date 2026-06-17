"""
Хэндлер профиля и навигации.
Содержит: профиль, главное меню, заглушки для билетов/депозита/акций.
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


@router.callback_query(F.data == "profile")
async def show_profile(callback: CallbackQuery):
    """Показать профиль пользователя из Telegram."""
    user = callback.from_user

    text = (
        f"👤 *Ваш профиль*\n\n"
        f"Имя: {user.first_name}\n"
        f"Username: @{user.username or 'не указан'}\n"
        f"ID: {user.id}\n"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ В меню", callback_data="main_menu")]
    ])

    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "main_menu")
async def back_to_menu(callback: CallbackQuery):
    """Возврат в главное меню (импортирует текст из start.py)."""
    from bot.handlers.start import WELCOME_TEXT

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

    await callback.message.edit_text(
        WELCOME_TEXT.format(name="Venue Club"),
        reply_markup=kb,
        parse_mode="Markdown",
    )
    await callback.answer()


@router.callback_query(F.data == "tickets")
async def show_tickets(callback: CallbackQuery):
    """Заглушка — раздел билетов (будет в v1.2)."""
    text = (
        "🎫 *Билеты*\n\n"
        "Раздел билетов будет доступен в следующей версии.\n"
        "Следите за обновлениями!"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ В меню", callback_data="main_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "deposit")
async def show_deposit(callback: CallbackQuery):
    """Заглушка — раздел депозитов (будет в v1.2)."""
    text = (
        "💳 *Депозит*\n\n"
        "Раздел депозитов будет доступен в следующей версии.\n"
        "Следите за обновлениями!"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ В меню", callback_data="main_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "promos")
async def show_promos(callback: CallbackQuery):
    """Заглушка — раздел акций (будет в v1.3)."""
    text = (
        "🎁 *Акции*\n\n"
        "Раздел акций будет доступен в следующей версии.\n"
        "Следите за обновлениями!"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ В меню", callback_data="main_menu")]
    ])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()
