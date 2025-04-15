# =============================================================================
# Title: define the database connection and session
# Date: 12, Apr 2025
# Author: Ted Jung
# Description: This code sets up an asynchronous database connection using SQLAlchemy and asyncmy.
#       Asynchronous database drivers (like asyncpg for PostgreSQL, asyncmy for MySQL, 
#       aiosqlite for SQLite, motor for MongoDB) 
# Result: This non-blocking I/O allows your application to serve many more concurrent users
#       with the same resources, leading to better scalability.
# =============================================================================

import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+asyncmy://root:pass@localhost:3306/myweb?charset=utf8"
engine = create_async_engine(DATABASE_URL)

# Create a async session object from session factory
# associate it with the engine (asyncsession -> engine)
# use session to interact with the database
Ted_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base is the declarative base class for SQLAlchemy ORM
# It provides a base class for declarative models.
# Declarative models are classes that define the structure of database tables
# and the relationships between them.
# The declarative base class maintains a catalog of classes and tables relative to that base.
# It also provides a registry for the classes and tables, allowing SQLAlchemy to map
# the classes to the tables and vice versa.
# This is the base class for all models in the application.
# It is used to create the database schema and manage the database connection.


Base = declarative_base()

async def create_tables():
    async with engine.begin() as conn:
        await Base.metadata.create_all(conn)
        # await conn.run_sync(Base.metadata.create_all)


        