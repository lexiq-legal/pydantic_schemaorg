from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class MusicVenue(CivicStructure):
    """A music venue.

    See https://schema.org/MusicVenue.

    """
    type_: str = Field("MusicVenue", const=True, alias='@type')
    

MusicVenue.update_forward_refs()
