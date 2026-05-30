from pydantic_settings import BaseSettings
from typing import List
import os
# dotenv module
from dotenv import load_dotenv
import cloudinary
load_dotenv()


class Settings(BaseSettings):
    # project info
    PROJECT_NAME : str = "Gallery Vault"
    VERSION : str = '0.0.1'


    # SERVER
    DEBUG : bool = True
    PSQL_DATABASE_URL : str = os.getenv('PSQL_DATABASE_URL')

    # JWT AUTH

    # CORS ORIGINS
    ALLOWED_ORIGINS : List[str] = [
        'http://localhost:5173'
    ]

    # FIREBASE
    FIREBASE_PROJECT_ID     : str = os.getenv("FIREBASE_PROJECT_ID")


    # CLOUDINARY
    
    CLOUDINARY_CLOUD_NAME   : str = os.getenv('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_CLOUD_API    : str = os.getenv('CLOUDINARY_CLOUD_API')
    CLOUDINARY_CLOUD_SECRET : str = os.getenv('CLOUDINARY_CLOUD_SECRET')

    # ENV CONFIG
    model_config={
        'env_file':'.env',
        'case_sensitive':True
    }

    print("NAME:", CLOUDINARY_CLOUD_NAME)
    print("API:", CLOUDINARY_CLOUD_API)
    print("SECRET:", CLOUDINARY_CLOUD_SECRET)

settings = Settings()
