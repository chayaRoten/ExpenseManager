import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from flask import Flask, render_template, request
from app.routes.user_router import user_router
from app.routes.budget_management_router import budget_management_router
from app.routes.visualization_router import visualization_router
from app.routes.ss import app1


app = FastAPI()
# app = Flask(__name__)

app.include_router(user_router, prefix='/user')
app.include_router(budget_management_router, prefix='/budget')
app.include_router(visualization_router, prefix='/visualization')
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
    app1.run(debug=True)
