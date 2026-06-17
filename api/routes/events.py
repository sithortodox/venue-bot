"""
API роутер — мероприятия.
CRUD операции: список, детали, создание.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.db.database import get_db
from api.models.models import Event
from api.schemas.schemas import EventCreate, EventResponse

router = APIRouter()


@router.get("/", response_model=list[EventResponse])
async def list_events(db: AsyncSession = Depends(get_db)):
    """GET /api/events/ — список всех активных мероприятий."""
    result = await db.execute(select(Event).where(Event.is_active == True))
    return result.scalars().all()


@router.get("/{event_id}", response_model=EventResponse)
async def get_event(event_id: int, db: AsyncSession = Depends(get_db)):
    """GET /api/events/{id} — детали одного мероприятия."""
    result = await db.execute(select(Event).where(Event.id == event_id))
    event = result.scalar_one_or_none()
    if not event:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Мероприятие не найдено")
    return event


@router.post("/", response_model=EventResponse)
async def create_event(data: EventCreate, db: AsyncSession = Depends(get_db)):
    """POST /api/events/ — создать мероприятие (для админки)."""
    event = Event(**data.model_dump())
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event
