from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    price: float
    description: str
    quantity: int


class MenuItemCreate(MenuItemBase):
    pass

class MenuUpdate(MenuItemBase):
    description : Optional[str]=None
    id: int
    price : Optional[float]=None
    quantity : Optional[int]=None

class MenuItem(MenuItemBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True