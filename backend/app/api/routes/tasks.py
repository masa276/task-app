from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.task import TaskCreate
from app.crud.task import create_task, get_tasks

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task, user_id=1)

@router.get("/")
def read(db: Session = Depends(get_db)):
    return get_tasks(db, user_id=1)
