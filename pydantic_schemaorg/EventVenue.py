from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class EventVenue(CivicStructure):
    """An event venue.

    See: https://schema.org/EventVenue
    Model depth: 4
    """
    type_: str = Field("EventVenue", alias='@type')
    

