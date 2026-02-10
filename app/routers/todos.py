from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[schemas.TodoOut])
async def get_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Todo))
    return result.scalars().all()


@router.get("/{todo_id}", response_model=schemas.TodoOut)
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Todo).where(models.Todo.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("/", response_model=schemas.TodoOut, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: schemas.TodoCreate, db: AsyncSession = Depends(get_db)):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo


@router.put("/{todo_id}", response_model=schemas.TodoOut)
async def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Todo).where(models.Todo.id == todo_id))
    db_todo = result.scalar_one_or_none()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo_update.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)

    await db.commit()
    await db.refresh(db_todo)
    return db_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Todo).where(models.Todo.id == todo_id))
    db_todo = result.scalar_one_or_none()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    await db.delete(db_todo)
    await db.commit()
    return None