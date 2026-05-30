from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class FirebaseAuthRequest(BaseModel):
    token : str

class UserResponse(BaseModel):
    id:int
    firebase_uid:str
    username:str
    email:str
    profile_image:Optional[str]
    provider:str
    created_at:datetime

    model_config = {
        'from_attributes':True,
        'extra':'forbid'
    }