from fastapi import Header,HTTPException,status,Depends
from sqlalchemy.orm import Session
from firebase_admin import auth
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from app.models import User
from app.core.database import get_db
security = HTTPBearer()

async def sync_auth_to_db_user(decoded_token,db):
    
    firebase_uid = decoded_token['uid']
    email = decoded_token['email']

    user = ( db.query(User)
            .filter(User.firebase_uid == firebase_uid) 
            .first()
        )
    
    if user:
        return user

    user = User(
        firebase_uid=firebase_uid,
        email=email
    )

    db.add(user)
    db.commit(user)
    db.refresh(user)

    return user

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

        user = await sync_auth_to_db_user(
            decoded_token,
            db
        )
        
        return user
    
    except Exception as e:
        print("FIREBASE VERIFY ERROR",e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid firebase token'
        )

