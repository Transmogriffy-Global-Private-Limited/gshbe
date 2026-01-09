from piccolo.table import Table
from piccolo.columns import UUID, Varchar, Integer, Float


class HelperPersonal(Table):
    id = UUID(primary_key=True)
    registration = UUID()
    name = Varchar()
    age = Integer()
    faith = Varchar()
    languages = Varchar()
    city = Varchar()
    area = Varchar()
    phone = Varchar()
    years_of_experience = Integer()
    avg_rating = Float(default=0)
    rating_count = Integer(default=0)
