# routes/uploads.py

import json

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    UploadFile
)

from sqlalchemy.orm import Session
from app.models import User
from app.core.database import get_db
from app.core.dependencies import verify_firebase_token,get_current_user

from app.schemas.image_schema import FileMetadata
from app.services.image_uploads.upload_service import UploadService

from app.services.image_service import ImageService
from app.schemas.image_schema import ImageResponse

router = APIRouter()


@router.post("/uploads")
async def upload_images(
    files: list[UploadFile] = File(...),
    metadata: str = Form(...),
    user: dict = Depends( get_current_user ),
    db: Session = Depends( get_db )
):

    db_user = db.query(User).filter(user.uid == User.firebase_uid)

    metadata_json = json.loads(metadata)

    print("METADATA JSON",metadata_json)

   
    parsed_metadata = [
        FileMetadata(**item)
        for item in metadata_json
    ]

    service = UploadService(db)

    return await service.upload_images(
        files=files,
        metadata=parsed_metadata,
        user=user
    )

@router.get('/images',response_model=list[ImageResponse])
async def images(
    db : Session = Depends(get_db),
    user : dict  = Depends(get_current_user)
    ):

    service = ImageService(db)
    images = await service.get_user_images(user)

    return images


@router.post('/remove-image/{image_id}')
async def remove_image(
    image_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    service = ImageService(db)
    return await service.remove_image(image_id, user)
