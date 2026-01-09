from piccolo.table import Table
from piccolo.columns import UUID, Varchar


class Registration(Table):
    id = UUID(primary_key=True)   # ✅ MUST be id
    role = Varchar()
    capacity = Varchar()
    profile_kind = Varchar()
