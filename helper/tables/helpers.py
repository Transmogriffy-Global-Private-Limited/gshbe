# helper/tables/helpers.py

from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey, Integer

from helper.tables.institutional import HelperInstitutional
from helper.tables.personal import HelperPersonal


class Helper(Table):
    institutional = ForeignKey(
        references=HelperInstitutional,
        null=True,
        related_name="helpers",
    )

    personal = ForeignKey(
        references=HelperPersonal,
        null=True,
        related_name="helpers",
    )

    is_active = Integer(default=1)
