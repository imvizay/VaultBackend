

from sqlalchemy.orm import Session
from app.services.auth.createuser import create_user

from app.core.database import get_db


from fastapi import APIRouter , Depends
router = APIRouter(
    prefix='/auth',
    tags=["Auth"]
)

from app.core.dependencies import verify_firebase_token
from app.services.users.users import fetch_all_users



@router.post('/sync')
async def register_user(db:Session = Depends(get_db),
                        decoded_token:dict=Depends(verify_firebase_token)):

    return create_user(decoded_token,db)




@router.get('/')
async def get_all_users(
    db: Session = Depends(get_db)
):

    users = fetch_all_users(db)

    return {
        "message": "Users fetched successfully",
        "users": users
    }