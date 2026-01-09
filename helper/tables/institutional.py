from piccolo.table import Table
from piccolo.columns import ForeignKey, Text, Integer
from helper.tables.registration import Registration


class HelperInstitutional(Table):
    registration = ForeignKey(Registration)

    institution_name = Text()
    city = Text()
    area = Text()
    phone = Text()
    avg_rating = Integer(default=0)
    rating_count = Integer(default=0)
