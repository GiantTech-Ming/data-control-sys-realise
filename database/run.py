from network import app
from database import init_db

if __name__ == "__main__":

    init_db()   # 启动数据库连接

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )