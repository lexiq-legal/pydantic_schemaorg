from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field.

    See: https://schema.org/SportsActivityLocation
    Model depth: 4
    """
    type_: str = Field("SportsActivityLocation", alias='@type')
    

