"""
API роутер — бронирования.
Создание заявки, список, обновление статуса.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.db.database import get_db
from api.models.models import Booking
from api.schemas.schemas import BookingCreate, BookingResponse

router = APIRouter()


@router.get("/", response_model=list[BookingResponse])
async def list_bookings(db: AsyncSession = Depends(get_db)):
    """GET /api/bookings/ — список всех бронирований."""
    result = await db.execute(select(Booking))
    return result.scalars().all()


@router.post("/", response_model=BookingResponse)
async def create_booking(data: BookingCreate, db: AsyncSession = Depends(get_db)):
    """POST /api/bookings/ — создать заявку на бронирование (из бота)."""
    booking = Booking(**data.model_dump())
    db.add(booking)
    await db.commit()
    await db.refresh(booking)
    return booking


@router.patch("/{booking_id}/status")
async def update_booking_status(
    booking_id: int,
    status: str,
    db: AsyncSession = Depends(get_db),
):
    """PATCH /api/bookings/{id}/status — обновить статус бронирования (для админки)."""
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    booking = result.scalar_one_or_none()
    if not booking:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    booking.status = status  # pending → confirmed / cancelled
    await db.commit()
    return {"status": "ok"}
