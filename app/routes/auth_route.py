from fastapi import APIRouter

router = APIRouter(
    prefix='/auth'
)

# LOGIN CLIENT
@router.get('/login')
async def login():
    pass
    

