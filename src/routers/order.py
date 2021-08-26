from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter,  Depends
from sqlalchemy.orm import Session
from core.schemas.menu import MenuItemCreate as MenuItemCreateSchema
from core.schemas.order import OrderCreate as OrderCreateSchema
from service import order as orderDAO
from core.database import SessionLocal
from routers.utils import *


router = APIRouter(
    tags=["order"],
    responses={404: {"description": "Not found"}}
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", status_code=200)
async def read_orders(db: Session=Depends(get_db)):
    try:
        retObj = orderDAO.get_orders(db)
        if type(retObj) is dict and 'error' in retObj:
            return setResponse(422, returnBodyJson=retObj)
        else: return retObj
    except Exception as e:
        logger.exception("Exception occurred while trying to get orders")
        return setResponse(500, str(e))

@router.get("/{id}", status_code=200)
async def read_order(id: int, db: Session=Depends(get_db)):
    try:
        retObj = orderDAO.get_order(db, id)
        if type(retObj) is dict and 'error' in retObj:
            return setResponse(422, returnBodyJson=retObj)
        else: return retObj
    except Exception as e:
        logger.exception("Exception occurred while trying to get orders")
        return setResponse(500, str(e))

@router.post("/", status_code=201)
async def create_order(order: OrderCreateSchema , db: Session=Depends(get_db)):
    try:
        retObj = orderDAO.create_order(db, order)
        if type(retObj) is dict and 'error' in retObj:
            return setResponse(422, returnBodyJson=retObj)
        else: return retObj
    except Exception as e:
        logger.exception("Exception occurred while trying to create order")
        return setResponse(500, str(e))



