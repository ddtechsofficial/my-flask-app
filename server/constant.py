DBNAME="crud_app"
DBHOST="localhost"
DBUSER="root"
DBPASSWORD="Password@123"


import os

DBHOST = os.environ.get("MYSQL_HOST", "localhost")
DBUSER = os.environ.get("MYSQL_USER", "root")
DBPASSWORD = os.environ.get("MYSQL_PASSWORD", "Password@123")
DBNAME = os.environ.get("MYSQL_DATABASE", "crud_app")