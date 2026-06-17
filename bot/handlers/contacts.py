"""
Хэндлер контактов администратора.
Показывает Telegram, телефон и кнопки быстрой связи.
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


@router.callback_query(F.data == "contacts")
async def show_contacts(callback: CallbackQuery):
    """Показать контакты с кнопками связи."""
    text = (
        "📞 *Контакты администратора*\n\n"
        "Есть вопросы? Напишите нам:\n"
        "• Telegram: @venue_admin\n"
        "• Телефон: +7 (999) 123-45-67\n"
        "• Время работы: 18:00 — 06:00\n\n"
        "Или нажмите кнопку ниже:"
    )

    # Кнопки: написать в Telegram, позвонить, вернуться в меню
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать в Telegram", url="https://t.me/venue_admin")],
        [InlineKeyboardButton(text="📞 Позвонить", url="tel:+79991234567")],
        [InlineKeyboardButton(text="◀️ В меню", callback_data="main_menu")],
    ])

    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()
