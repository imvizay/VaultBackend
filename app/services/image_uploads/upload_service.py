# services/upload_service.py

import uuid

from fastapi import HTTPException
from app.schemas.image_schema import FileMetadata
from app.models.image_model import Image
from app.services.image_uploads.cloudinary_service import CloudinaryService


class UploadService:

    def __init__(self, db):
        self.db = db

    async def upload_images(
        self,
        files,
        metadata,
        user
    ):
        print("USER",user)


        uploaded_cloudinary_ids = []

        try:

            image_records = []

            for file, meta in zip(files, metadata):

                # -------------------
                # FILE SIZE
                # -------------------

                file.file.seek(0, 2)
                size = file.file.tell()
                file.file.seek(0)

                if size == 0:
                    raise HTTPException(
                        400,
                        "Empty file"
                    )

                public_id = (
                    f"gallery-vault/"
                    f"{user.firebase_uid}/"
                    f"{uuid.uuid4()}"
                )

                # -------------------
                # CLOUDINARY
                # -------------------

                upload_result = (
                    CloudinaryService.upload_file(
                        file=file.file,
                        public_id=public_id
                    )
                )

                uploaded_cloudinary_ids.append(
                    upload_result["public_id"]
                )
                
                image = Image(
                    user_id = user.id,
                    user_uid=user.firebase_uid,
                    public_id=upload_result["public_id"],
                    image_url=upload_result["secure_url"],
                    iv=meta.iv,
                    mime_type=meta.originalType,
                    original_name=meta.originalName,
                    size=size
                )

                image_records.append(image)

            # -------------------
            # SAVE ALL RECORDS
            # -------------------

            self.db.add_all(image_records)

            self.db.commit()

            return {
                "success": True,
                "uploaded": len(image_records)
            }

        except Exception as e:

            print("ERROR : ",e)

            self.db.rollback()

            # -------------------
            # COMPENSATION
            # -------------------

            for public_id in uploaded_cloudinary_ids:

                try:
                    CloudinaryService.delete_file(
                        public_id
                    )
                except Exception:
                    pass

            raise HTTPException(
                status_code=500,
                detail=str(e)
            )