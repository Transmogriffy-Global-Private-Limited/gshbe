from piccolo.table import Table
from piccolo.columns import UUID, Varchar
import uuid


class Registration(Table):
    registration_id = UUID(primary_key=True, default=uuid.uuid4)
    role = Varchar()
    capacity = Varchar()
    profile_kind = Varchar()
