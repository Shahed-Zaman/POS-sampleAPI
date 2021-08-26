from sqlalchemy.orm import Session
from core.models.menu import MenuItem as MenuItemModel
from core.schemas.menu import MenuItemCreate as MenuItemCreateSchema
from core.schemas.menu import MenuItem as MenuItemSchema
from utils.logger import logger


def create_menu_item(db: Session, item: MenuItemCreateSchema):
    logger.debug("Adding new menu item: %s" % item)
    new_item = MenuItemModel(price=item.price, description=item.description, quantity=item.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    logger.debug("Successfully added menu item to DB; item: %s" % new_item)
    return new_item


def get_menu_item(db: Session, id: int):
    logger.debug("Querying DB to get menu item details for item id: %s" % id)
    itemFound = db.query(MenuItemModel).filter(MenuItemModel.id == id).first()
    logger.debug("Found the following item details for id: %s; item: %s" % (id, itemFound))
    return itemFound


def get_menu_items(db: Session):
    logger.debug("Querying DB to get all menu items")
    itemsFound = db.query(MenuItemModel).all()
    logger.debug("Found %s menu items in DB" % len(itemsFound))
    return itemsFound


def update_menuitem(db: Session, item: MenuItemSchema):
    logger.debug("Updating menu item (id: %s) with details: %s" % (item.id, item))

    itemFoundInDB = db.query(MenuItemModel).filter(MenuItemModel.id == item.id).first()

    if not itemFoundInDB:
        errstr = "No record found to update with id: %s" % item.id
        return {'error': errstr}

    if item.price: itemFoundInDB.price = item.price
    if item.description: itemFoundInDB.description = item.description
    if item.quantity: itemFoundInDB.quantity = item.quantity
    db.commit()
    db.refresh(itemFoundInDB)
    logger.debug("Successfully updated menu item (id: %s); new details: %s" % (item.id, itemFoundInDB))
    return itemFoundInDB


def delete_menuitem(db: Session, id: int):
    logger.debug("Deleting menu item (id: %s)" % id)
    itemInDB = get_menu_item(db, id)
    if itemInDB is None:
        logger.warning("No item with id %s found to delete from DB" % id)
        return False
    else:
        db.delete(itemInDB)
        db.commit()
        logger.debug("Successfully deleted item (id: %s)" % id)
        return True
