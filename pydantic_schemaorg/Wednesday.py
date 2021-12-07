from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Wednesday(DayOfWeek):
    """The day of the week between Tuesday and Thursday.

    See https://schema.org/Wednesday.

    """
    type_: str = Field("Wednesday", const=True, alias='@type')
    

Wednesday.update_forward_refs()
