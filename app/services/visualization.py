import requests
import matplotlib.pyplot as plt

async def visualizationDef():
    # שליפת הנתונים מהשרת
    response = requests.get('http://127.0.0.1:8000/budget?userId=1')
    # בדיקת קוד תגובה
    if response.status_code == 200:
        data = response.json()  # המרת התגובה ל JSON
        # יצירת ויזואליזציה מתאימה (לדוגמה, גרף)
        plt.plot(data['revenues'], data['expenses'], marker='o', linestyle='-')

        # הגדרת כותרת וכווץ
        plt.title('Visualization of Data')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # הצגת הוויזואליזציה
        plt.show()
    else:
        print("Failed to fetch data from server. Status code:", response.status_code)
