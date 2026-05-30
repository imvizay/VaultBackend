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
    DEBUG : bool = os.getenv("DEBUG")
    DATABASE_URL : str = os.getenv('DATABASE_URL')

    # JWT AUTH

    # CORS ORIGINS
    FRONTEND_URL : str = os.getenv('FRONTEND_URL')

    # FIREBASE
    FIREBASE_PROJECT_ID     : str = os.getenv("FIREBASE_PROJECT_ID")


    # CLOUDINARY
    
    CLOUDINARY_NAME   : str = os.getenv('CLOUDINARY_NAME')
    CLOUDINARY_API_KEY    : str = os.getenv('CLOUDINARY_API_KEY')
    CLOUDINARY_SECRET : str = os.getenv('CLOUDINARY_SECRET')

    # ENV CONFIG
    model_config={
        'env_file':'.env',
        'case_sensitive':True
    }

settings = Settings()
