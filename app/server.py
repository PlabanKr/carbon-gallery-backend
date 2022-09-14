from fastapi import FastAPI

from .routers import users
from .db import models
from .db.main import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root_route():
    return {"message": "Backend for carbon gallery"}