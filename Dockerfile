# Multi-stage Dockerfile — три образа: bot, api, webapp

# === Базовый образ (Python) ===
FROM python:3.12-slim AS base

WORKDIR /app

# Установка зависимостей для PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# === Telegram-бот ===
FROM base AS bot
CMD ["python", "-m", "bot.main"]

# === FastAPI бэкенд ===
FROM base AS api
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

# === Mini App (React + Vite) ===
FROM node:20-alpine AS webapp
WORKDIR /app
COPY webapp/package*.json ./
RUN npm ci
COPY webapp/ .
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
