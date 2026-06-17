"""
FSM-состояния для диалога бронирования.
Каждый шаг — отдельное состояние конечного автомата.
"""
from aiogram.fsm.state import State, StatesGroup


class BookingForm(StatesGroup):
    """Шаги диалога бронирования (4 шага)."""
    event_name = State()   # Шаг 1: название мероприятия
    name = State()         # Шаг 2: имя гостя
    phone = State()        # Шаг 3: телефон
    guest_count = State()  # Шаг 4: количество гостей
