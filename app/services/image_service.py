from app.models.image_model import Image
from fastapi import HTTPException
import cloudinary.uploader

class ImageService:
    def __init__(self,db):
        self.db = db

    async def get_user_images(self,user):

        images = (
            self.db.query(Image)
            .filter(Image.user_id == user.id)
            .order_by(Image.uploaded_at.desc())
            .all()
        )

        return images
    
    async def remove_image(self,image_id,user):
        image = ( self.db.query(Image)
                 .filter(Image.id == image_id )
                 .first()
        )

        if not image:
            raise HTTPException(
                status_code=404,
                detail="Image not found"
            )

        if image.user_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )
        

        result = cloudinary.uploader.destroy(
            public_id=image.public_id,
            resource_type='raw'
        )

        if result['result'] not in ['ok','not found']:
            raise HTTPException(
                500,
                "Cloudinary deletion failed"
            )
        
        self.db.delete(image)

        self.db.commit()

        return {
            "success": True
        }
            
