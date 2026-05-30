from sqlalchemy.orm import Session
from fastapi import HTTPException,status

from app.models.user_model import User



def create_user(decoded_token,db:Session):


    # Existing User
    existing_user = db.query(User).filter(
        User.email == decoded_token.get('email')
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash Password
   
    # print("DECODED TOKEN",decoded_token)
    provider = decoded_token.get('firebase',{}).get('sign_in_provider','email')

    print("PROVDER",provider)

    # Create User Object
    new_user = User(
        firebase_uid=decoded_token.get('uid'),
        username=decoded_token.get("email").split('@')[0],
        email=decoded_token.get("email"),
        provider=provider
      
    )

    # Save to Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        'message':'User created successfully',
        'user':{
            'id':new_user.id,
            "username":new_user.username,
            'email':new_user.email
        }
    }