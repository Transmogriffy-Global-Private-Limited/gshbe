from piccolo.table import Table
from piccolo.columns import UUID, Varchar


class Registration(Table):
    role = Varchar()
    capacity = Varchar()
