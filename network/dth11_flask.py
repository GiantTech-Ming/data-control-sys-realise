from . import app
from flask import jsonify
import random

# 温湿度
@app.route("/chart")
def chart():
    return jsonify({
        "temperature": round(random.uniform(20,30),2),
        "humidity": round(random.uniform(40,70),2)
    })


# 农田数据
@app.route("/farm")
def farm():
    return jsonify({
        "soil": round(random.uniform(30,70),2),
        "light": random.randint(200,800),
        "ph": round(random.uniform(5.5,7.5),2)
    })


# 害虫数据
@app.route("/pest")
def pest():
    return jsonify({
        "aphid": random.randint(0,20),
        "armyworm": random.randint(0,15),
        "beetle": random.randint(0,10)
    })