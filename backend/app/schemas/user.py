from pydantic import BaseModel, EmailStr
from typing import Optional

# --- ユーザー作成用スキーマ ---
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

# --- ユーザー応答用スキーマ ---
class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True  # SQLAlchemy モデルを Pydantic に変換可能にする

# --- トークン関連スキーマ ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
