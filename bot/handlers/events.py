"""
Хэндлеры афиши мероприятий.
Загружает список мероприятий из API и показывает карточки.
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import httpx

from bot.config import get_settings

router = Router()


@router.callback_query(F.data == "events")
async def list_events(callback: CallbackQuery):
    """Показать список ближайших мероприятий (до 5 штук)."""
    settings = get_settings()

    # Запрос мероприятий из API
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{settings.api_url}/api/events/", timeout=5)
            events = resp.json() if resp.status_code == 200 else []
    except Exception:
        events = []

    # Если мероприятий нет — показываем заглушку
    if not events:
        await callback.message.edit_text(
            "📅 *Афиша мероприятий*\n\n"
            "Пока нет запланированных мероприятий.\n"
            "Следите за обновлениями!",
            parse_mode="Markdown",
        )
        await callback.answer()
        return

    # Формируем текстовый список мероприятий
    text = "📅 *Ближайшие мероприятия:*\n\n"
    for ev in events[:5]:
        text += (
            f"🎭 *{ev['title']}*\n"
            f"📅 {ev['date']}\n"
            f"💰 {ev.get('price', 'Уточняйте')}\n\n"
        )

    # Инлайн-кнопки для выбора мероприятия
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=ev["title"], callback_data=f"event_{ev['id']}")]
        for ev in events[:5]
    ])
    kb.inline_keyboard.append(
        [InlineKeyboardButton(text="◀️ Назад", callback_data="main_menu")]
    )

    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data.startswith("event_"))
async def event_detail(callback: CallbackQuery):
    """Показать детали конкретного мероприятия."""
    event_id = callback.data.split("_")[1]
    settings = get_settings()

    # Запрос данных мероприятия из API
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{settings.api_url}/api/events/{event_id}", timeout=5)
            ev = resp.json() if resp.status_code == 200 else None
    except Exception:
        ev = None

    if not ev:
        await callback.answer("Мероприятие не найдено", show_alert=True)
        return

    # Формируем карточку мероприятия
    text = (
        f"🎭 *{ev['title']}*\n\n"
        f"📅 {ev['date']}\n"
        f"📍 {ev.get('venue', 'Территория клуба')}\n"
        f"💰 {ev.get('price', 'Уточняйте')}\n\n"
        f"{ev.get('description', '')}"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 Связаться с админом", callback_data="contacts")],
        [InlineKeyboardButton(text="◀️ К афише", callback_data="events")],
    ])

    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()
