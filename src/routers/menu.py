from fastapi import APIRouter,  Depends
from sqlalchemy.orm import Session
from core.schemas.menu import MenuItemCreate as MenuItemCreateSchema
from core.schemas.menu import MenuUpdate as MenuUpdateSchema
from core.schemas.menu import MenuItem as MenuItemSchema
from service import menu as menuDAO
from core.database import SessionLocal
from routers.utils import *

router = APIRouter(
    tags=["menu"],
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
async def read_menu(db: Session=Depends(get_db)):
    try:
        items = menuDAO.get_menu_items(db)
        if items is None or len(items) == 0:   return setResponse(404)
        else:
            return items
    except Exception as e:
        logger.exception("Exception occurred while trying to get menu items")
        return setResponse(500, str(e))


@router.get("/{id}", status_code=200)
async def read_menuitem(id: int, db: Session=Depends(get_db)):
    try:
        item = menuDAO.get_menu_item(db, id)
        if item is not None:  return item
        else: return setResponse(404)
    except Exception as e:
        logger.exception("Exception occured while trying to get menu item details for id: %s" %id)
        return setResponse(500, str(e))


@router.post("/", status_code=201)
async def create_menuitem(item: MenuItemCreateSchema, db: Session=Depends(get_db)):
    try:
        return menuDAO.create_menu_item(db, item)
    except Exception as e:
        logger.exception("Exception occurred while trying to save new menu item to DB. Item details: %s" %item)
        return setResponse(500, str(e))


@router.put("/", status_code=204)
async def update_menuitem(item: MenuUpdateSchema, db: Session=Depends(get_db)):
    try:
        retObj = menuDAO.update_menuitem(db, item)
        if type(retObj) is dict and 'error' in retObj:
            return setResponse(500, returnBodyJson=retObj)
        else:
            return retObj
    except Exception as ex:
        logger.exception("Exception occurred while trying to update menu item; id=%s" %item.id)
        return setResponse(500, str(ex))


@router.delete("/{id}", status_code=200)
async def delete_menuitem(id: int, db: Session=Depends(get_db)):
    try:
        if not menuDAO.delete_menuitem(db, id):
            return setResponse(404, "Failed to delete id %s; perhaps, id was not found" %id)
    except Exception as ex:
        logger.exception("Exception occurred while trying to delete menu item; id=%s" %id)
        return setResponse(500, str(ex))