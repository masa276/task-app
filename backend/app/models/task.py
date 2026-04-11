from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # 外部キー
    user_id = Column(Integer)

    # ⭐重要：文字列で参照（import禁止）
    #user = relationship("User", back_populates="tasks")
