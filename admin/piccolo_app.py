# admin/piccolo_app.py
from piccolo.conf.apps import AppConfig

APP_CONFIG = AppConfig(
    app_name="admin",
    migrations_folder_path="admin/piccolo_migrations",
    table_classes=[
        "admin.tables.admin.Admin",
    ],
)
