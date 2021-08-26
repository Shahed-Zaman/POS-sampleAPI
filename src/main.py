from fastapi import Depends, FastAPI
from routers import menu, order
from core.database import Base, engine
import os

# Create DB
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(menu.router, prefix="/menu")
app.include_router(order.router, prefix="/order")


@app.get("/")
async def root():
    return {"message": "Hello POS Application!"}
