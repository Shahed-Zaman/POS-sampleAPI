from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text, CheckConstraint, Table
from sqlalchemy.orm import relationship

from core.database import Base, engine

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(Text)
    payment = Column(Float)
    items = relationship('OrderItem', backref='Order', lazy='dynamic')

class OrderItem(Base):
    __tablename__ = "orderitems"
    id = Column(Integer, primary_key=True, index=True)
    orderId = Column('order_id', Integer, ForeignKey("order.id"))
    itemId = Column('item_id', Integer, ForeignKey("menu.id"))
    price = Column('price', Float)
    quantity = Column('quantity', Integer)
