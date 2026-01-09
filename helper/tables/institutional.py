from piccolo.table import Table
from piccolo.columns import UUID, Varchar, Integer


class HelperInstitutional(Table):
    registration = UUID(primary_key=True)

    name = Varchar()
    city = Varchar(null=True)
    address = Varchar(null=True)
    phone = Varchar(null=True)

    avg_rating = Varchar(default="0")
    rating_count = Integer(default=0)
