from piccolo.table import Table
from piccolo.columns import (
    Serial,
    UUID,
    Varchar,
    Integer,
)


class HelperPersonal(Table):
    id = Serial(primary_key=True)
    registration = UUID()
    name = Varchar()
    age = Integer()
    faith = Varchar(null=True)
    languages = Varchar(null=True)
    city = Varchar(null=True)
    area = Varchar(null=True)
    phone = Varchar(null=True)
    years_of_experience = Integer(null=True)
    avg_rating = Varchar(default="0")
    rating_count = Integer(default=0)
