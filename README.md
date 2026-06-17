# Venue Bot — Telegram Bot + Mini App

Telegram-бот и Mini App для клуба/ивент- площадки. Гости смотрят афишу, бронируют столы, связываются с администратором.

## Стек

| Компонент | Технология |
|-----------|-----------|
| Telegram Bot | Python 3.12, aiogram 3.x |
| Backend API | FastAPI, SQLAlchemy 2.0 (async) |
| Database | PostgreSQL 16 |
| Cache | Redis 7 |
| Mini App | React 18, Vite, TailwindCSS |
| Deploy | Docker Compose |

## Быстрый старт

### 1. Клонировать и настроить

```bash
git clone https://github.com/your-org/venue-bot.git
cd venue-bot
cp .env.example .env
```

### 2. Заполнить `.env`

```env
BOT_TOKEN=your_bot_token
ADMIN_TELEGRAM_ID=your_id
MINI_APP_URL=https://your-domain.com/app
```

### 3. Запустить

```bash
docker compose up -d
```

### 4. Инициализировать БД и наполнить тестовыми данными

```bash
docker compose exec api python -m scripts.seed_events
```

### 5. Открыть

- **Бот:** `t.me/your_bot`
- **Mini App:** `http://localhost:3000`
- **API:** `http://localhost:8000/health`

## Структура проекта

```
venue-bot/
├── bot/                    # Telegram бот (aiogram)
│   ├── handlers/           # Хэндлеры команд
│   ├── keyboards/          # Инлайн-клавиатуры
│   ├── middlewares/         # Middleware (БД, антивлуд)
│   └── states/             # FSM-состояния
├── api/                    # FastAPI бэкенд
│   ├── models/             # SQLAlchemy модели
│   ├── schemas/            # Pydantic схемы
│   ├── routes/             # API эндпоинты
│   └── db/                 # Подключение к БД
├── webapp/                 # Mini App (React + Vite)
│   └── src/pages/          # Экраны приложения
├── scripts/                # Утилиты (seed, миграции)
├── docker-compose.yml
└── .env.example
```

## Эндпоинты API

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/events/` | Список мероприятий |
| `GET` | `/api/events/{id}` | Детали мероприятия |
| `POST` | `/api/events/` | Создать мероприятие |
| `GET` | `/api/bookings/` | Список бронирований |
| `POST` | `/api/bookings/` | Создать бронирование |
| `PATCH` | `/api/bookings/{id}/status` | Обновить статус |
| `GET` | `/api/users/{telegram_id}` | Профиль пользователя |
| `GET` | `/health` | Health check |

## Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Приветствие и главное меню |
| `📅 Афиша` | Список мероприятий |
| `📞 Связаться` | Контакты администратора |
| `👤 Мой профиль` | Профиль пользователя |
| `🎫 Билеты` | Раздел билетов (скоро) |
| `💳 Депозит` | Раздел депозитов (скоро) |
| `🎁 Акции` | Акции и промокоды (скоро) |

## лицензия

MIT
