from pymysql.cursors import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()

database = {
    "host"          : os.getenv("DB_HOST"),
    "port"          : int(os.getenv("DB_PORT")),
    "user"          : os.getenv("DB_USERNAME"),
    "password"      : os.getenv("DB_PASSWORD"),
    "db"            : os.getenv("DB_DATABASE"),
    "charset"       : 'utf8mb4',
    "autocommit"    : True,
    "cursorclass"   : DictCursor
}

environment = os.getenv("ENV")

frontend_uri = os.getenv("FRONTEND_URI")

sendgrid = os.getenv("SENDGRID")

maps_token = os.getenv("MAPS_TOKEN")
ipstack = os.getenv("IPSTACK_TOKEN")
