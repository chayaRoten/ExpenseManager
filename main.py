import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routes.user_router import user_router
from app.routes.budget_management_router import budget_management_router

app = FastAPI()
app.include_router(user_router, prefix='/user')
app.include_router(budget_management_router, prefix='/budget')
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
# @app.on_event('startup')
# async def print_something():
#     print("something")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)