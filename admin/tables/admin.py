from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, Timestamp
from datetime import datetime


class Admin(Table):
    email = Varchar(unique=True, index=True)
    password_hash = Varchar()
    is_active = Boolean(default=True)
    created_at = Timestamp(default=datetime.utcnow)
