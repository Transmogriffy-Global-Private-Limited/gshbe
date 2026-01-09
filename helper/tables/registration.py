from piccolo.table import Table
from piccolo.columns import Text, UUID
import uuid


class Registration(Table):
    id = UUID(primary_key=True, default=uuid.uuid4)

    role = Text()
    capacity = Text()
    profile_kind = Text()
