from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Thursday(DayOfWeek):
    """The day of the week between Wednesday and Friday.

    See https://schema.org/Thursday.

    """

    locals().update({"@type": Field("Thursday", const=True)})


Thursday.update_forward_refs()
