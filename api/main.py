"""
FastAPI приложение — бэкенд для Telegram-бота и Mini App.
Предоставляет REST API для мероприятий, бронирований и пользователей.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import events, bookings, users

# Создание FastAPI приложения
app = FastAPI(title="Venue Bot API", version="1.0.0")

# CORS — разрешаем все origins для демо (в продакшене ограничить)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров (API эндпоинтов)
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["bookings"])
app.include_router(users.router, prefix="/api/users", tags=["users"])


@app.get("/health")
async def health_check():
    """Проверка работоспособности API."""
    return {"status": "ok"}
