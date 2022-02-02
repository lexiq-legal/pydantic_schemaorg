from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque.

    See: https://schema.org/NightClub
    Model depth: 5
    """
    type_: str = Field("NightClub", alias='@type')
    

