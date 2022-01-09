from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from app.models import *
from utils import get_session

router = APIRouter()

@router.get("/users", response_model=List[UserRead])
async def get_users(*, session: Session=Depends(get_session)):
    statement = select(User)
    results = session.exec(statement).all()
        
    return results

@router.post("/tasks", response_model=List[TaskRead])
async def get_tasks(user: UserQuery, session: Session=Depends(get_session)):
    statement = select(Task).where(Task.owner_id == user.id)
    results = session.exec(statement).all()

    return results

@router.post("/task", response_model=TaskRead)
async def get_task(task: TaskQuery, session: Session=Depends(get_session)):
    statement = select(Task).where(Task.owner_id == task.owner_id and Task.id == task.id)
    result = session.exec(statement).one_or_none()

    return result

@router.post("/create/task", response_model=StandardResponse)
async def create_task(task: TaskCreate, session: Session=Depends(get_session)):
    db_task = Task.from_orm(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return StandardResponse()

@router.post("/create/user", response_model=StandardResponse)
async def create_user(user: UserCreate, session: Session=Depends(get_session)):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return StandardResponse()

@router.post("/delete/task", response_model=StandardResponse)
async def delete_task(task: TaskQuery, session: Session=Depends(get_session)):
    statement = select(Task).where(Task.id == task.id and Task.owner_id == task.owner_id)
    result = session.exec(statement)
    task = result.one_or_none()
    if task:
        session.delete(task)
        session.commit()
        return StandardResponse()
    return StandardResponse(success="Failure", message="Invalid Task id or Owner id", code=400)

@router.post("/delete/user", response_model=StandardResponse)
async def delete_user(user: UserQuery, session: Session=Depends(get_session)):
    statement = select(User).where(User.id == user.id)
    result = session.exec(statement)
    user = result.one_or_none()
    if user:
        session.delete(user)
        session.commit()
        return StandardResponse()
    return StandardResponse(success="Failure", message="Invalid User id", code=400)

@router.post("/update/task", response_model=StandardResponse)
async def update_task(task: TaskRead, session: Session=Depends(get_session)):
    task = Task.from_orm(task)
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return StandardResponse()