from fastapi import Header,HTTPException,status,Depends
from sqlalchemy.orm import Session
from firebase_admin import auth
from app.models import User
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

from app.core.database import get_db
security = HTTPBearer()




async def verify_firebase_token(
    credentials : HTTPAuthorizationCredentials = Depends(security),
    db:Session = Depends(get_db)
    ):
        
    try:
        print("INSIDE TOKEN DEPENDCY")
        print(f"CREDENTIALS : - {credentials}")
        
        token = credentials.credentials
        
        print("token",token)
        
        decoded_token = auth.verify_id_token(token)
        
        return decoded_token
    
    except Exception as e:
        print("FIREBASE VERIFY ERROR",e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid firebase token'
        )



async def get_current_user(
    decoded_token=Depends(verify_firebase_token),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(
            User.firebase_uid == decoded_token["uid"]
        )
        .first()
    )

    if not user:
        raise HTTPException(
            404,
            "User not found"
        )

    return user
