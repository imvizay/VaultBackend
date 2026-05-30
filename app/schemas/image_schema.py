# schemas/image.py

from pydantic import BaseModel
from datetime import datetime


class FileMetadata(BaseModel):
    iv: str
    originalName: str
    originalType: str
    size: int

class ImageResponse(BaseModel):

    id: int 
    public_id: str  
    image_url: str  
    iv: str 
    mime_type: str  
    original_name: str  
    size: int   
    uploaded_at: datetime

    class Config:
        from_attributes = True