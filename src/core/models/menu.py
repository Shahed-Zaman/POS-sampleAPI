from sqlalchemy import Boolean, Column, Integer, Float, Text, CheckConstraint

from core.database import Base, engine
import json

class MenuItem(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    description = Column(Text)
    quantity = Column(Integer, default=0)

    __table_args__ = (
        CheckConstraint('quantity >= 0', name="menuitem_quantity_non_negative"),
    )

    def __str__(self):
        return "tablename: %s, id: %s, price: %s, description: %s, quantity: %s" %(self.__tablename__, self.id, self.price, self.description, self.quantity)
