from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class MusicVenue(CivicStructure):
    """A music venue.

    See https://schema.org/MusicVenue.

    """

    locals().update({"@type": Field("MusicVenue", const=True)})


MusicVenue.update_forward_refs()
