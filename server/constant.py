import os

# use public URL directly
MYSQL_URL = os.environ.get("MYSQL_PUBLIC_URL", None)

DBHOST = os.environ.get("MYSQLHOST", "localhost")
DBUSER = os.environ.get("MYSQLUSER", "root")
DBPASSWORD = os.environ.get("MYSQLPASSWORD", "Password@123")
DBNAME = os.environ.get("MYSQLDATABASE", "crud_app")
DBPORT = int(os.environ.get("MYSQLPORT", 3306))