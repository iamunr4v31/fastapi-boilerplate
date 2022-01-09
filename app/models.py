from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List


class UserBase(SQLModel):
    username: str
    desc: str

class User(UserBase, table=True):
    id: Optional[int] = Field(index=True, default=None, primary_key=True)
    password: str
    tasks: List["Task"] = Relationship(back_populates="owner")

class UserQuery(SQLModel):
    id: int

class UserCreate(UserBase):
    pass

class UserRead(UserBase, UserQuery):
    pass


class TaskBase(SQLModel):
    title: str
    desc: str
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner: Optional[User] = Relationship(back_populates="tasks")

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int

class TaskQuery(SQLModel):
    id: int
    owner_id: int


class StandardResponse(BaseModel):
    success: str = "Success"
    message: str = "Task completed successfully"
    code: int = 200