from pydantic import Field
from pydantic_schema_org.DayOfWeek import DayOfWeek


class Tuesday(DayOfWeek):
    """The day of the week between Monday and Wednesday.

    See https://schema.org/Tuesday.

    """

    locals().update({"@type": Field("Tuesday", const=True)})


Tuesday.update_forward_refs()
