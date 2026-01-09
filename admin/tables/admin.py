from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, Timestamp
from datetime import datetime


class Admin(Table):
    name = Varchar(length=100)
    phone_number = Varchar(length=15, unique=True, index=True)
    password_hash = Varchar()
    is_active = Boolean(default=True)
    created_at = Timestamp(default=datetime.utcnow)
