# =============================================================================
# Title: Defined three Pydantic models
# Date: 13, Apr 2025
# Author: Ted Jung
# Description: Data validation and serialization for the API.
# =============================================================================

from pydantic import BaseModel


# inherit from BaseModel
# to define the schema for data validation and serialization
# using Pydantic
class ItemBase(BaseModel):
    name: str
    description: str
    price: int

# Inherit from ItemBase
# to define the schema for creating an item
# pass: doesn't have any additional fields
class ItemCreate(ItemBase):
    pass

# Inherit from ItemBase
# to define the additional fields for the item
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True