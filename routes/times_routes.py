from fastapi import APIRouter
router = APIRouter()
@router.get('/api/v1/times')
async def get_times():
    return {"info" : "Times"}

