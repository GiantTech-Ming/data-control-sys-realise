# -*- coding: utf-8 -*-
from .SqlUtil import execute
from datetime import datetime

def insert_env_data(temperature, humidity):

    sql = """
    INSERT INTO env_data
    (temperature, humidity, collect_time)
    VALUES (%s,%s,%s)
    """

    execute(sql, (
        temperature,
        humidity,
        datetime.now()
    ))

def select_user(username, password):
    sql = """
    SELECT * FROM user
    WHERE username = %s AND password = %s
    """
    execute(sql, (
        username, password
    ))