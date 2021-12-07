from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic_schemaorg.CivicStructure import CivicStructure


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    """A stadium.

    See https://schema.org/StadiumOrArena.

    """
    type_: str = Field("StadiumOrArena", const=True, alias='@type')
    

StadiumOrArena.update_forward_refs()
