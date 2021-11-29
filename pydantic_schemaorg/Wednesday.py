from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Wednesday(DayOfWeek):
    """The day of the week between Tuesday and Thursday.

    See https://schema.org/Wednesday.

    """

    locals().update({"@type": Field("Wednesday", const=True)})


Wednesday.update_forward_refs()
