"""Point d'entré de FastAPI"""

from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="API REST pour gérer des tâches",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Task Manager API", "status": "ok"}