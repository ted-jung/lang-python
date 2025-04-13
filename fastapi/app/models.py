# =============================================================================
# Title: Define the database model
# Date: 12, Apr 2025
# Author: Ted Jung
# Description: This code defines the database model for an item using SQLAlchemy ORM.
# =============================================================================

from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    description = Column(String(30))
    price = Column(Integer)