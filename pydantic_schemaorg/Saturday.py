from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Saturday(DayOfWeek):
    """The day of the week between Friday and Sunday.

    See https://schema.org/Saturday.

    """
    type_: str = Field("Saturday", const=True, alias='@type')
    

Saturday.update_forward_refs()
