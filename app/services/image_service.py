from app.models.image_model import Image

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