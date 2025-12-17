from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import ForeignKey


ID = "2025-12-17T10:19:20:195749"
VERSION = "1.30.0"
DESCRIPTION = "registration_account_unique"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="db", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="Registration",
        tablename="registration",
        column_name="account",
        db_column_name="account",
        params={"unique": True},
        old_params={"unique": False},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    return manager
