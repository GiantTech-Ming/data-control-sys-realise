# database/sqlite_db.py
# SQLite数据库模块

import sqlite3

class SQLiteDB:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or [])
        self.connection.commit()
        return cursor.fetchall()