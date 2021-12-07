from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Monday(DayOfWeek):
    """The day of the week between Sunday and Tuesday.

    See https://schema.org/Monday.

    """
    type_: str = Field("Monday", const=True, alias='@type')
    

Monday.update_forward_refs()
