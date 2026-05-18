from mysql.connector import connect
from server.constant import DBHOST, DBNAME, DBPASSWORD, DBUSER
def db_connect():
    try:
        return connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASSWORD
        )
    except Exception as e:
        print("Error while connecting to DB: ", e)
