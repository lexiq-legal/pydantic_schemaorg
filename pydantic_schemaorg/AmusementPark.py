from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """An amusement park.

    See: https://schema.org/AmusementPark
    Model depth: 5
    """
    type_: str = Field("AmusementPark", alias='@type')
    

