from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Tuesday(DayOfWeek):
    """The day of the week between Monday and Wednesday.

    See https://schema.org/Tuesday.

    """
    type_: str = Field("Tuesday", const=True, alias='@type')
    

Tuesday.update_forward_refs()
