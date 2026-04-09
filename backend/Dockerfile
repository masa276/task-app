# Python 3.11
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 10000

# Renderは環境変数を自動で読み込む
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
