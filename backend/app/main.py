from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine

# ルーターをインポート
from app.api.routes import auth, tasks
from app.models import user, task
app = FastAPI(
    title="Task Management App",
    description="A simple task management app with FastAPI and React",
    version="1.0.0"
)

# CORS設定（フロントエンドからアクセスする場合必須）
origins = [
    "http://localhost:5173",  # ViteフロントエンドURL（開発環境）
    "https://your-frontend-domain.com"  # デプロイ先URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

# ルートエンドポイント（簡易確認用）
@app.get("/")
def root():
    return {"message": "Task Management API is running"}
