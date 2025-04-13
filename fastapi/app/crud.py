# =============================================================================
# Title: Transactional CRUD operations
# Date: 13, Apr 2025    
# Author: Ted Jung
# Description: This code defines the CRUD operations for an item in a FastAPI application.
# =============================================================================


from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Item
from app.schema import ItemCreate

async def get_items(db: AsyncSession):
    return await db.query(Item).all()

async def get_item(db: AsyncSession, item_id: int):
    return await db.query(Item).filter(Item.id == item_id).first()

async def create_item(db: AsyncSession, item: ItemCreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def update_item(db: AsyncSession, item: Item, updated_item: ItemCreate):
    for key, value in updated_item.model_dump().items():
        setattr(item, key, value)
    await db.commit()
    await db.refresh(item)
    return item

async def delete_item(db: AsyncSession, item: Item):
    await db.delete(item)
    await db.commit()