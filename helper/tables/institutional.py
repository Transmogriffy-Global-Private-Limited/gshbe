# helper/tables/institutional.py

from piccolo.table import Table
from piccolo.columns import Varchar, Integer


class HelperInstitutional(Table):
    name = Varchar(length=255)
    code = Varchar(length=100, unique=True)
    is_active = Integer(default=1)
