from database.SqlUtil import execute
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