from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models.task import TaskStatus

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Build TaskFlow API",
                "description": "Complete the FastAPI backend project",
                "status": "pending"
            }
        }

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

    class Config:
        json_schema_extra = {
            "example": {
                "status": "in_progress"
            }
        }

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: TaskStatus
    owner_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]
    total: int
    limit: int
    offset: int

    class Config:
        json_schema_extra = {
            "example": {
                "tasks": [],
                "total": 0,
                "limit": 10,
                "offset": 0
            }
        }
