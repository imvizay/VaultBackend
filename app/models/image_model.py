from sqlalchemy import Integer,Column,String,Boolean,DateTime,ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime,UTC

class Image(Base):
   
   __tablename__="images"

   id = Column(Integer,primary_key=True)

   user_id = Column(Integer,ForeignKey("users.id"))
   user_uid = Column(String,nullable=False)
   public_id = Column(String,nullable=False)

   image_url = Column(String,nullable=False)

   iv = Column(String,nullable=False)

   mime_type = Column(String,nullable=False)

   original_name = Column(String,nullable=False)

   size = Column(String,nullable=False)

   uploaded_at = Column(DateTime,default=lambda:datetime.now(UTC))

   # FORWARD RELATION    
   user = relationship('User',back_populates='images')



  