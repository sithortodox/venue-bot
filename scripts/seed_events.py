"""
Скрипт заполнения БД тестовыми мероприятиями.
Запуск: python -m scripts.seed_events
"""
import asyncio
from datetime import datetime, timedelta

from api.db.database import engine, async_session
from api.models.models import Base, Event


async def seed():
    """Создаёт таблицы и заполняет 4 тестовыми мероприятиями."""
    # Создание таблиц (если их нет)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Вставка тестовых данных
    async with async_session() as session:
        events = [
            Event(
                title="Night Party",
                description="Лучшая вечеринка города! DJ-сет, коктейли, атмосфера.",
                date=datetime.now() + timedelta(days=3),
                venue="Main Hall",
                price="от 1500₽",
            ),
            Event(
                title="Lounge Evening",
                description="Спокойный вечер в lounge-зоне. Живая музыка, крафтовые напитки.",
                date=datetime.now() + timedelta(days=5),
                venue="Terrace",
                price="от 1000₽",
            ),
            Event(
                title="VIP Night",
                description="Эксклюзивное мероприятие для VIP-гостей. Ограниченное количество мест.",
                date=datetime.now() + timedelta(days=7),
                venue="VIP Zone",
                price="от 3000₽",
            ),
            Event(
                title="Rooftop Sunset",
                description="Встречаем закат на крыше. Коктейли, закуски, живая атмосфера.",
                date=datetime.now() + timedelta(days=10),
                venue="Rooftop",
                price="от 2000₽",
            ),
        ]

        session.add_all(events)
        await session.commit()
        print("✅ Тестовые данные созданы!")


if __name__ == "__main__":
    asyncio.run(seed())
