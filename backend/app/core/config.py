import os

# Renderでは .env は不要
# 必要な環境変数はすべて Renderの Environment Variables で設定

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# 起動時に不足していたらエラーを出す
if not DATABASE_URL or not SECRET_KEY:
    raise RuntimeError("DATABASE_URL or SECRET_KEY is not set in Environment Variables")
