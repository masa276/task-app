from fastapi import FastAPI
from app.api.routes import auth, tasks

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "Task API running"}
