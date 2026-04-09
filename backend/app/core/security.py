from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from jose import JWTError, jwt

from app.core.config import settings

# パスワードハッシュ化用
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- パスワード関連 ---

def hash_password(password: str) -> str:
    """パスワードをハッシュ化"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """平文パスワードとハッシュを比較"""
    return pwd_context.verify(plain_password, hashed_password)

# --- JWTトークン関連 ---

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    JWTトークン作成
    data: トークンに含める情報 (例: {"sub": email})
    expires_delta: 有効期限 (デフォルト: settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """
    JWTトークンをデコード
    トークン無効の場合は JWTError を送出
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError as e:
        raise e
