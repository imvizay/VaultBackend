from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import app.core.cloudinary.cloudinary_config
from .core.firebase import firebase_config
# Setting
from app.core.settings import settings
# DATABASE

# ROUTES
from app.routes import all_routes

# FAST INSTANCE
app = FastAPI(
    title="GalleryVault webapp",
    version='0.0.1',
    description="Gallery Vault Backend API",
    docs_url="/docs",
    redoc_url="/redoc",
    # lifespan=lifespan
)

# MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
async def root():
    return {
        'message':'Gallery vault backend is running'
    }

# URLS
for route in all_routes:
    app.include_router(route,prefix='/api')


# GLOBAL EXCEPTION HANDLER
@app.exception_handler(Exception)
async def global_exception_handler(request,exception):
    print(f"ERROR,{exception}")

    return JSONResponse (
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )



