# schema for create task, update task, get task
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List

class TaskBase(BaseModel):
    title: str
    description: str
    status: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

