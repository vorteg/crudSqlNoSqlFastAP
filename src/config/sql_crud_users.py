from sqlalchemy.orm import Session

# Local modules
from data.models import users_model
from data.schemas import schema_users


def create_user(db: Session, user: schema_users.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = users_model.UserModel(email=user.email,
                                    hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users_model.UserModel).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(users_model.UserModel).filter(users_model.UserModel.
                                                  id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(users_model.UserModel).filter(users_model.UserModel.
                                                  email == email).first()
