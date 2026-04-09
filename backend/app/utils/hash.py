from passlib.context import CryptContext

# パスワードハッシュ化用の設定
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- パスワードハッシュ化 ---
def hash_password(password: str) -> str:
    """
    平文パスワードをハッシュ化して返す
    """
    return pwd_context.hash(password)

# --- パスワード検証 ---
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    平文パスワードとハッシュ化パスワードを比較
    """
    return pwd_context.verify(plain_password, hashed_password)
