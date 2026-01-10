from piccolo.conf.apps import AppConfig

class AdminAppConfig(AppConfig):
    app_name = "admin"
    migrations_folder_path = "admin/piccolo_migrations"
