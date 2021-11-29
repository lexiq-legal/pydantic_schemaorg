from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Friday(DayOfWeek):
    """The day of the week between Thursday and Saturday.

    See https://schema.org/Friday.

    """

    locals().update({"@type": Field("Friday", const=True)})


Friday.update_forward_refs()
