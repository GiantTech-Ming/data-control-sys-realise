from flask import Flask, request, jsonify
import pymysql
from database import db

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    name = data.get("name")
    password = data.get("password")

    cursor = db.cursor()

    sql = "SELECT name,password FROM users WHERE name=%s"

    cursor.execute(sql,(name,))

    user = cursor.fetchone()

    if user and user[1] == password:

        return jsonify({
            "status":"success"
        })

    return jsonify({
        "status":"fail"
    })


app.run(host="0.0.0.0",port=5000)