from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    """A health club.

    See: https://schema.org/HealthClub
    Model depth: 5
    """
    type_: str = Field(default="HealthClub", alias='@type', const=True)
    
