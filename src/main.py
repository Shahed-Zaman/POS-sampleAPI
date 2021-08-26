from fastapi import Depends, FastAPI
from dependencies import get_token_header
from routers import menu, order
from core.database import Base, engine
import os

# Create DB
Base.metadata.create_all(bind=engine)

if "AUTH_TOKEN" in os.environ: dependency =  [Depends(get_token_header)]
else: dependency = []

app = FastAPI(dependencies=dependency)
app.include_router(menu.router, prefix="/menu")
app.include_router(order.router, prefix="/order")


@app.get("/")
async def root():
    return {"message": "Hello POS Application!"}
