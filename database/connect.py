# -*- coding: utf-8 -*-
#connect.py
from pymysql import Connection

con = Connection(
    host='192.168.88.226',
    port=3306,
    user='root',
    password='6666'
)

print(type(con))

con.close()