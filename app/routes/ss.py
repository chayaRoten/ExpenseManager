from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import requests

app1 = Flask(__name__)



@app1.route('/plot', methods=['POST'])
def plot():
    response = requests.get('http://127.0.0.1:8000/budget?userId=1')
    if response.status_code == 200:
        data = response.json()
        plt.plot(data['revenues'], data['expenses'], marker='o', linestyle='-')
        plt.title('Visualization of Data')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()
    # plt.savefig('static/plot.png')
    # return render_template('plot.html')
        return ""


if __name__ == '__main__':
    app1.run(debug=True)
