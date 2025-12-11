# db/piccolo_conf.py
from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "gshbedb",
        "user": "postgres",
        "password": "Tgpldev2025",
        "host": "localhost",
        "port": 5432,
    }
)

# Register your app(s)
APP_REGISTRY = AppRegistry(apps=["db.piccolo_app"])
