import cloudinary
from ..settings import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_SECRET,
    secure=True
)
print("CLOUDINARY INITIATED")