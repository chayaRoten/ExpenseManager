from fastapi import APIRouter, HTTPException
from app.services import visualization as vl

visualization_router = APIRouter()


@visualization_router.post('/plot')
# @visualization_router.post('/plot')
async def visualization():
    """"""
    try:
        await vl.plot()
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in visualization")
    return f"visualization"
