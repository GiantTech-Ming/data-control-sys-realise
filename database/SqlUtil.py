from database import db

def execute(sql, params=None):
    cursor = db.cursor()

    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    db.commit()
    cursor.close()


def query(sql):
    cursor = db.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()

    cursor.close()
    return result