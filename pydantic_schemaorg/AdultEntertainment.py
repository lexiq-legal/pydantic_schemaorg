from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment.

    See: https://schema.org/AdultEntertainment
    Model depth: 5
    """
    type_: str = Field("AdultEntertainment", alias='@type')
    

