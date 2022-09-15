from fastapi import FastAPI

from .routers import users, images
from .db import models
from .db.main import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(images.router)

@app.get("/")
def root_route():
    return {"message": "Backend for carbon gallery"}