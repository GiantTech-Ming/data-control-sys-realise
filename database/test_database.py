# -*- coding: utf-8 -*-
# 测试数据库连接、写入和读取

from database import init_db
from database.SqlUtil import execute, query

def test_database():
    # 初始化数据库连接
    db = init_db()
    assert db is not None, "数据库连接失败"

    # 创建测试表
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS test_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        value INT NOT NULL
    ) ENGINE=InnoDB;
    """
    execute(create_table_sql)

    # 插入测试数据
    insert_sql = "INSERT INTO test_table (name, value) VALUES (%s, %s)"
    execute(insert_sql, ("test_name", 123))

    # 查询测试数据
    select_sql = "SELECT * FROM test_table WHERE name = 'test_name'"
    result = query(select_sql)

    assert len(result) == 1, "数据插入失败或查询失败"
    assert result[0][1] == "test_name", "查询结果不匹配"
    assert result[0][2] == 123, "查询结果不匹配"

    print("数据库测试通过！")

if __name__ == "__main__":
    test_database()