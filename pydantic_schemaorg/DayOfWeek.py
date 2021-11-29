from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DayOfWeek(Enumeration):
    """The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification"
     "refer. Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1)"
     "were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]],"
     "[[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have"
     "now been integrated directly into schema.org.

    See https://schema.org/DayOfWeek.

    """

    locals().update({"@type": Field("DayOfWeek", const=True)})


DayOfWeek.update_forward_refs()
