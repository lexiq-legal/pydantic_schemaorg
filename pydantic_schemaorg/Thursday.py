from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Thursday(DayOfWeek):
    """The day of the week between Wednesday and Friday.

    See https://schema.org/Thursday.

    """
    type_: str = Field("Thursday", const=True, alias='@type')
    

Thursday.update_forward_refs()
