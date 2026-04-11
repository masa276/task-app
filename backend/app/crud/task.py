from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate


def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(
        title=task.title,
        description=task.description,
        user_id=user_id
    )

    db.add(db_task)
    db.commit()          # ★必須
    db.refresh(db_task)  # ★必須

    return db_task
