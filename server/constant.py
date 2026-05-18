# DBNAME="crud_app"
# DBHOST="localhost"
# DBUSER="root"
# DBPASSWORD="Password@123"


import os

DBHOST = os.environ.get("MYSQLHOST", "localhost")
DBUSER = os.environ.get("MYSQLUSER", "root")
DBPASSWORD = os.environ.get("MYSQLPASSWORD", "Password@123")
DBNAME = os.environ.get("MYSQLDATABASE", "crud_app")
DBPORT = int(os.environ.get("MYSQLPORT", 3306))
