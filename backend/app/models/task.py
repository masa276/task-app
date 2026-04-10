from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    # 👇 ここがセット
    user = relationship("User", back_populates="tasks")
