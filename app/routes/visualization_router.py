from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from app.services import visualization as vl
import requests
visualization_router = APIRouter()
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
app = Flask(__name__)

@visualization_router.get('')
async def visualization():
    """"""
    try:
        vis = await vl.visualizationDef()
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred in visualization")
    return f"{vis}"



# @app.route('/plot', methods=['POST'])
# def plot():
#     response = requests.get('http://127.0.0.1:8000/budget?userId=1')
#     if response.status_code == 200:
#         data = response.json()  # המרת התגובה ל JSON
#         # יצירת ויזואליזציה מתאימה (לדוגמה, גרף)
#         plt.plot(data['revenues'], data['expenses'], marker='o', linestyle='-')
#
#         # הגדרת כותרת וכווץ
#         plt.title('Visualization of Data')
#         plt.xlabel('X-axis')
#         plt.ylabel('Y-axis')
#         # הצגת הוויזואליזציה
#         plt.show()
#     plt.savefig('static/plot.png')
#     return render_template('plot.html')
#
