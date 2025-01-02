from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Union

class ItemBase(BaseModel):
    name: str
    price: PositiveFloat
    is_offer: Union[bool, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int