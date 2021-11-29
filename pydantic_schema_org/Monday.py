from pydantic import Field
from pydantic_schema_org.DayOfWeek import DayOfWeek


class Monday(DayOfWeek):
    """The day of the week between Sunday and Tuesday.

    See https://schema.org/Monday.

    """

    locals().update({"@type": Field("Monday", const=True)})


Monday.update_forward_refs()
