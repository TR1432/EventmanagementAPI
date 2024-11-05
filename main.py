from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Event
from schemas import Event as EventSchema
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/events")
def get_all_events(db: Session = Depends(get_db)):
    events = db.execute(select(Event)).scalars().all()
    return events


@app.post("/events")
async def item(db:Session = Depends(get_db), data: EventSchema | None = None):
    event = Event(**data.model_dump())
    db.add(event)
    db.commit()
    
    return event

@app.get("/events/{event_id}")
async def get_event(event_id: int | None = None , db: Session = Depends(get_db)):
    event = db.get(Event, event_id)
    if event is None :
        raise HTTPException(status_code=404, detail="Events not found")
    return event

@app.delete("/events/{event_id}")
async def delete_event(event_id: int | None = None , db: Session = Depends(get_db)):
    event = db.get(Event, event_id)
    db.delete(event)
    db.commit()
    return {"message": f"Event {event_id} is Successfully deleted"}
