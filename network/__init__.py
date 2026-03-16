# network/__init__.py
# 网络通信模块初始化
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../web/templates",
    static_folder="../web/static"
)

# 首页
@app.route("/")
def index():
    return render_template("index.html")

# 图表页
@app.route("/chart_page")
def chart_page():
    return render_template("chart.html")


# 导入 API
from . import dth11_flask