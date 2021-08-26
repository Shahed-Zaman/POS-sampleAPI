from typing import List
from pydantic import BaseModel
from typing import Optional


class OrderItem(BaseModel):
    id: int
    quantity: int


class OrderBase(BaseModel):
    items: List[OrderItem]


class OrderCreate(OrderBase):
    note: Optional[str] = None
    payment: Optional[float] = None


class Order(OrderBase):
    id: Optional[int] = None
    note: Optional[str] = None

    class Config:
        orm_mode = True


class OrderViewItem(OrderItem):
    description: Optional[str]
    price: Optional[float]


class OrderView(Order):
    items: List[OrderViewItem]
    payment: float
