# create the router for create tasks, get tasks, update tasks user wize
# logged in user can only access their own tasks

from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import Optional
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from app.dependencies import current_user_id
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.task import Task
from app.schemas.task import TaskResponse, TaskUpdate, TaskCreate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/")
def create_task(task: TaskCreate, user_id: UUID=Depends(current_user_id),db: Session=Depends(get_db)):
    task_model = Task(**task.model_dump(), user_id=user_id)
    db.add(task_model)
    db.commit()
    db.refresh(task_model)
    return task_model

@router.get("/", response_model=Page[TaskResponse])
def get_tasks(
    user_id: UUID = Depends(current_user_id),
    db: Session = Depends(get_db),
    status: Optional[str] = None,
):
    query = db.query(Task).filter(Task.user_id == user_id)
    if status:
        query = query.filter(Task.status == status)
    query = query.order_by(Task.created_at.asc())
    return paginate(db, query)

@router.put("/{task_id}")
def update_task(task_id: int, user_id: UUID=Depends(current_user_id),db: Session=Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
    
