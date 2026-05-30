from .auth_route import  router as auth_router
from .image_route import router as image_router 
from .user_route import  router as user_router

all_routes = [  
    auth_router,
    image_router,
    user_router
]
