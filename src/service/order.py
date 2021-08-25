from sqlalchemy.orm import Session
from ..core.models.menu import MenuItem as MenuItemModel
from ..core.schemas.order import Order as OrderSchema
from ..core.models.order import OrderItem as OrderItemModel
from ..core.models.order import Order as OrderModel
from ..core.models.order import OrderItem as OrderItemModel
from ..core.schemas.order import OrderView as OrderViewModel
from ..core.schemas.order import OrderViewItem as OrderViewItemModel



from ..core.schemas.menu import MenuItem as MenuItemSchema
from ..utils.logger import logger
from ..service import menu as menuDAO

def create_order(db: Session, order: OrderSchema) -> dict:
    logger.debug("Creating new order; order received: %s" %order)
    if len(order.items) == 0:
        errStr = "0 items provdied in Order"
        return {'error': errStr}

    newOrderObj = OrderModel()
    newOrderObj.note = order.note
    newOrderObj.payment = order.payment
    orderTotal = 0
    for orderItem in order.items:
        # get some more menu item details from DB
        orderDetails = menuDAO.get_menu_item(db, orderItem.id)
        if orderDetails is None:
            errStr = "Cannot find any item in DB with id: %s" %orderItem.id
            logger.warning(errStr)
            return {'error': errStr}

        orderTotal += orderDetails.price * orderItem.quantity
        orderDetails.quantity -= orderItem.quantity
        newOrderObj.items.append(OrderItemModel(quantity=orderItem.quantity, itemId=orderItem.id, price=orderDetails.price))

    # if no payment amount is provided, use the calculated amount as total
    if order.payment is None: newOrderObj.payment = orderTotal
    elif orderTotal > order.payment:
        errStr = "Provided order payment %s is too low, should be at least %s" %(order.payment, orderTotal )
        logger.warning(errStr)
        return {'error': errStr}

    # save in DB
    db.add(newOrderObj)
    db.commit()
    db.refresh(newOrderObj)
    logger.debug("Order id: %s,  payment: %s" %(newOrderObj.id, newOrderObj.payment))
    logger.debug("Successfully order with id: %s" %newOrderObj.id)
    return {'orderid':newOrderObj.id}

def get_orders(db: Session) -> dict:
    logger.debug("Querying DB to get all orders")
    itemsFound = db.query(OrderModel).all()
    logger.debug("Found %s orders in DB" %len(itemsFound))
    return itemsFound

def get_order(db: Session, id:int) -> dict:
    logger.debug("Querying DB to get order details for order id: %s" %id)
    itemsFound = db.query(OrderModel, MenuItemModel, OrderItemModel
                         ).filter(
                            OrderModel.id == id
                        ).filter(
                            OrderModel.id == OrderItemModel.orderId
                        ).filter(
                            OrderItemModel.itemId == MenuItemModel.id
                        ).all()
    if len(itemsFound) == 0: return None

    orderDetailsObj = OrderViewModel(items=[], payment=0)
    for item in itemsFound:
        orderDetailsObj.id = item['OrderItem'].orderId
        orderDetailsObj.note = item['Order'].note
        orderDetailsObj.payment = item['Order'].payment

        orderItemObj = OrderViewItemModel(id=0, quantity=0)
        orderItemObj.id = item['OrderItem'].itemId
        orderItemObj.quantity = item['OrderItem'].quantity
        orderItemObj.price = item['OrderItem'].price
        orderItemObj.description = item['MenuItem'].description

        orderDetailsObj.items.append(orderItemObj)

    logger.debug("Found following order details : %s" %(orderDetailsObj))
    return orderDetailsObj

def delete_order(db: Session, id:int) -> dict:

    return {}

