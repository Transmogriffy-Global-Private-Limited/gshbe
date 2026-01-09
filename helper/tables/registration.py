from piccolo.table import Table
from piccolo.columns import UUID, Varchar


class Registration(Table):
    registration_id = UUID(primary_key=True)
    role = Varchar()
    capacity = Varchar()
    profile_kind = Varchar()
