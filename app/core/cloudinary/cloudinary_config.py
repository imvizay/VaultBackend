import cloudinary
from ..settings import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_CLOUD_API,
    api_secret=settings.CLOUDINARY_CLOUD_SECRET,
    secure=True
)
print("CLOUDINARY INITIATED")