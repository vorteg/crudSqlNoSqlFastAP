from fastapi import FastAPI, Request, Response

from data.models import users_model as db 
from services.database import SessionLocal, engine


db.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GO Shrimp", description="Users Register & Products inventory to  Go Shrimp Restaurant", version="0.1.4")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency option 1
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


# Dependency option 1
# def get_db(request: Request):
#     return request.state.db
# Dependency option2
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
