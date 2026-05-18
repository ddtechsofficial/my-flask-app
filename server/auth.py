from server.db import db_connect

def  createUser(username, password):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO USERS (username, password) VALUES (%s, %s)", (username, password)
    )
    conn.commit()
    conn.close()


def getUserByUserName(username):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM USERS WHERE username=%s", (username, )
    )
    user = cursor.fetchone()
    conn.close()
    return  user

