from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment.

    See https://schema.org/AdultEntertainment.

    """
    type_: str = Field("AdultEntertainment", const=True, alias='@type')
    

AdultEntertainment.update_forward_refs()
