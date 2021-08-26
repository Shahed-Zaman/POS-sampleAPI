from sqlalchemy import Column, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import relationship
from core.database import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(Text)
    payment = Column(Float)
    items = relationship('OrderItem', backref='Order', lazy='dynamic')


class OrderItem(Base):
    __tablename__ = "orderitems"
    orderId = Column('order_id', Integer, ForeignKey("order.id"), primary_key=True)
    itemId = Column('item_id', Integer, ForeignKey("menu.id"), primary_key=True)
    item = relationship("MenuItem")
    price = Column('price', Float)
    quantity = Column('quantity', Integer)
