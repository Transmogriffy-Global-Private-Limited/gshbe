class Registration(Table):
    registration_id = UUID(primary_key=True)
    role = Varchar()
    capacity = Varchar()
    profile_kind = Varchar()
