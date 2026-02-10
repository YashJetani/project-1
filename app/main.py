from fastapi import FastAPI
from .routers import todos
from .database import engine, Base
from .config import settings

@app.get("/")
def root():
    return {
        "message": "Todo API is running! 🚀 Visit /api/v1/docs for interactive docs"
    }
app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(todos.router, prefix=settings.API_V1_STR)
