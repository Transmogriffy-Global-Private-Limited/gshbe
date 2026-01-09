from piccolo.table import Table
from piccolo.columns import (
    ForeignKey,
    Integer,
    Text,
)
from helper.tables.registration import Registration


class HelperPersonal(Table):
    registration = ForeignKey(Registration)

    name = Text()
    age = Integer()
    faith = Text()
    languages = Text()
    city = Text()
    area = Text()
    phone = Text()
    years_of_experience = Integer()
    avg_rating = Integer(default=0)
    rating_count = Integer(default=0)
