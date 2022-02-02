from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HealthClub(SportsActivityLocation, HealthAndBeautyBusiness):
    """A health club.

    See: https://schema.org/HealthClub
    Model depth: 5
    """
    type_: str = Field("HealthClub", alias='@type')
    

