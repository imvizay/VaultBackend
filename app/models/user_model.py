from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime,UTC


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)

    firebase_uid = Column(String,unique=True,nullable=False)

    username = Column(String,nullable=False,index=True,unique=True)

    email = Column(String,nullable=False,unique=True)

    profile_image = Column(String,nullable=True)

    # AUTH PROVIDER - github/facebook/google/email
    provider = Column(String,nullable=False)

    created_at = Column(DateTime,default = lambda:datetime.now(UTC))

    # Reverse Relation
    images = relationship("Image", back_populates="user", cascade="all, delete")
