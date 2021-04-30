from sqlalchemy import Boolean, Column,  Integer, String
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship

from services.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")
