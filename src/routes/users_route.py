from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


from config.app_config import app, get_db
from data.schemas import schema_users
from config import sql_crud_users

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(skip: int = 0,
                     limit: int = 100, db: Session = Depends(get_db)):
    users = sql_crud_users.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users/", response_model=schema_users.User, tags=["users"])
async def create_user(user: schema_users.UserCreate, db: Session = Depends(get_db)):
    db_user = sql_crud_users.get_user_by_email(db, email=user.email)
    if db_user:
         raise HTTPException(status_code=400, detail="Email already registered")
    return sql_crud_users.create_user(db=db, user=user)




@app.get("/users/id/{user_id}",
         response_model=schema_users.User, tags=["users"])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = sql_crud_users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/@/{email}",
         response_model=schema_users.User, tags=["users"])
async def user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = sql_crud_users.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
