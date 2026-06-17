"""
Хэндлер бронирования (FSM — конечный автомат).
Сценарий: мероприятие → имя → телефон → кол-во гостей → отправка заявки.
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from bot.states.booking_states import BookingForm
from bot.config import get_settings
import httpx

router = Router()


@router.callback_query(F.data == "booking")
async def start_booking(callback: CallbackQuery, state: FSMContext):
    """Начало бронирования — запрос названия мероприятия."""
    await callback.message.edit_text(
        "📞 *Быстрая заявка на бронирование*\n\n"
        "Введите название мероприятия или дату:",
        parse_mode="Markdown",
    )
    await state.set_state(BookingForm.event_name)  # Переход к следующему шагу
    await callback.answer()


@router.message(BookingForm.event_name)
async def process_event(message: Message, state: FSMContext):
    """Шаг 1: сохраняем название мероприятия, запрашиваем имя."""
    await state.update_data(event_name=message.text)
    await message.answer(
        "👤 *Ваше имя:*",
        parse_mode="Markdown",
    )
    await state.set_state(BookingForm.name)


@router.message(BookingForm.name)
async def process_name(message: Message, state: FSMContext):
    """Шаг 2: сохраняем имя, запрашиваем телефон."""
    await state.update_data(name=message.text)
    await message.answer(
        "📱 *Телефон:*",
        parse_mode="Markdown",
    )
    await state.set_state(BookingForm.phone)


@router.message(BookingForm.phone)
async def process_phone(message: Message, state: FSMContext):
    """Шаг 3: сохраняем телефон, запрашиваем количество гостей."""
    await state.update_data(phone=message.text)
    await message.answer(
        "👥 *Количество гостей:*",
        parse_mode="Markdown",
    )
    await state.set_state(BookingForm.guest_count)


@router.message(BookingForm.guest_count)
async def process_guests(message: Message, state: FSMContext):
    """Шаг 4: завершение — формируем заявку и отправляем в API."""
    data = await state.get_data()
    await state.update_data(guest_count=message.text)
    await state.clear()  # Очищаем FSM после завершения

    settings = get_settings()

    # Текст подтверждения для пользователя
    booking_text = (
        "✅ *Заявка создана!*\n\n"
        f"🎭 Мероприятие: {data['event_name']}\n"
        f"👤 Имя: {data['name']}\n"
        f"📱 Телефон: {data['phone']}\n"
        f"👥 Гостей: {message.text}\n\n"
        "Наш администратор свяжется с вами в ближайшее время!"
    )

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ В меню", callback_data="main_menu")]
    ])

    await message.answer(booking_text, reply_markup=kb, parse_mode="Markdown")

    # Текст уведомления для администратора
    admin_text = (
        "📋 *Новая заявка на бронирование*\n\n"
        f"🎭 {data['event_name']}\n"
        f"👤 {data['name']}\n"
        f"📱 {data['phone']}\n"
        f"👥 {message.text} гостей\n"
        f"🆔 Пользователь: {message.from_user.id}"
    )

    # Отправка заявки в API (бэкенд)
    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{settings.api_url}/api/bookings/",
                json={
                    "user_id": message.from_user.id,
                    "event_name": data["event_name"],
                    "name": data["name"],
                    "phone": data["phone"],
                    "guest_count": int(message.text),
                },
                timeout=5,
            )
    except Exception:
        pass  # В демо-режиме не крашимся, если API недоступен
