from fastapi import FastAPI
from .routers import todos
from .database import engine, Base
from .config import settings



@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(todos.router, prefix=settings.API_V1_STR)
