from pydantic import Field
from pydantic_schema_org.DayOfWeek import DayOfWeek


class Saturday(DayOfWeek):
    """The day of the week between Friday and Sunday.

    See https://schema.org/Saturday.

    """

    locals().update({"@type": Field("Saturday", const=True)})


Saturday.update_forward_refs()
