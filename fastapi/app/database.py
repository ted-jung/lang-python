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


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+asyncmy://root:pass@localhost:3306/myweb?charset=utf8"
engine = create_async_engine(DATABASE_URL)

# Create a session object from session factory
# associate it with the engine (session -> engine)
# use session to interact with the database
Ted_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")