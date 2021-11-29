from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Sunday(DayOfWeek):
    """The day of the week between Saturday and Monday.

    See https://schema.org/Sunday.

    """

    locals().update({"@type": Field("Sunday", const=True)})


Sunday.update_forward_refs()
