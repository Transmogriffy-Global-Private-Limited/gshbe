# db/piccolo_conf.py
from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine
import os

DB = PostgresEngine(
    config={
        "database": os.getenv("DBNAME"),
        "user": os.getenv("DBUSER"),
        "password": os.getenv("DBPASS"),
        "host": os.getenv("DBHOST"),
        "port": int(os.getenv("DBPORT", "5432")),
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "auth.piccolo_app",
        "profiles.piccolo_app",
        "helper.piccolo_app",
        "admin.piccolo_app",
    ]
)
