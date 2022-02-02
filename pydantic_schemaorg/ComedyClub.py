from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """A comedy club.

    See: https://schema.org/ComedyClub
    Model depth: 5
    """
    type_: str = Field("ComedyClub", alias='@type')
    

