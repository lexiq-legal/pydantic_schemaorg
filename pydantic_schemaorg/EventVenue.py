from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class EventVenue(CivicStructure):
    """An event venue.

    See https://schema.org/EventVenue.

    """
    type_: str = Field("EventVenue", const=True, alias='@type')
    

EventVenue.update_forward_refs()
