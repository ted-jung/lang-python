# =============================================================================
# Title: FastAPI CRUD API with Async I/O
# Date: 13, Apr 2025
# Author: Ted Jung
# Description: when working with databases in Python to build scalable and responsive applications, 
#        especially web APIs, that can handle many concurrent requests efficiently. 
#        Here are the key use cases:
#   1. **Asynchronous I/O**: Async I/O allows for non-blocking operations, 
#      meaning that while one operation is waiting for a response (like a database query),
#   2. **Concurrency**: Async I/O allows multiple operations to be in progress at the same time.
#   3. **Scalability**: Async I/O can handle a large number of concurrent connections
#      without requiring a large number of threads or processes.
#   4. **Performance**: Async I/O can improve performance in I/O-bound applications,
#      where the application spends a lot of time waiting for I/O operations to complete.
#   5. **Integration with Async Frameworks**: Many modern web frameworks (like FastAPI,
#      Starlette, and Sanic) are built on top of async I/O, allowing for seamless integration
#      with async database libraries.
#   6. **Event-Driven Architecture**: Async I/O is well-suited for event-driven architectures,
#      where the application responds to events (like incoming requests) rather than following a strict sequence of operations.
#   7. **Microservices**: In a microservices architecture, services often need to communicate with each other
#      over the network. Async I/O can help manage these network calls efficiently.
#   8. **Real-time Applications**: Async I/O is ideal for real-time applications,
#      such as chat applications or live data feeds, where low latency is crucial.
# =============================================================================

import asyncio

from fastapi import Request, FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, database, models, schema
from contextlib import asynccontextmanager


async def get_db():
    async with database.Ted_Session() as db:
        yield db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run before the application starts
    print("Application startup")
    await database.create_tables()
    # Initialize resources, connect to databases, etc.
    await asyncio.sleep(1)  # Example startup task
    yield
    # Code to run when the application shuts down
    print("Application shutdown")
    # Close connections, release resources, etc.
    await asyncio.sleep(1)  # Example shutdown task


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return RedirectResponse(url="/items/")


@app.get("/items/")
async def get_items(db: AsyncSession = Depends(get_db)):
    items = await crud.get_items(db)
    return items


@app.get("/items/{item_id}")
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items/")
async def create_item(item: schema.ItemCreate, db: AsyncSession=Depends(get_db)):
    db_item = await crud.create_item(db, item)
    return db_item


@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: schema.ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = await crud.update_item(db, db_item, updated_item)
    return updated_item


@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await crud.delete_item(db, db_item)
    return {"message": "Item deleted successfully"}


@app.get("/ted_home1/")
#async def root():
def ted_home1():
    return {"message": "Hello Ted World"}


@app.post("/ted_home2/")
async def ted_home2(request: Request):
    response = await request.json()
    return response


# Two options to run the server
# uvicorn: lightning-fast ASGI server implemented in pure Python
# > uvicorn app.main:app --reload --host 0.0.0.0 --port 9001

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9001)