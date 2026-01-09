from piccolo.table import Table
from piccolo.columns import UUID, Varchar


class Registration(Table):
    registration_id = UUID(primary_key=True)
    role = Varchar()              # helper / user / both
    capacity = Varchar()          # personal / institutional
    profile_kind = Varchar()      # helper_personal / helper_institutional
