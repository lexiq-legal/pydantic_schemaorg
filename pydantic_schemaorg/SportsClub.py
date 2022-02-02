from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """A sports club.

    See: https://schema.org/SportsClub
    Model depth: 5
    """
    type_: str = Field("SportsClub", alias='@type')
    

