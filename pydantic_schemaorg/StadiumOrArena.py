from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class StadiumOrArena(CivicStructure, SportsActivityLocation):
    """A stadium.

    See https://schema.org/StadiumOrArena.

    """
    type_: str = Field("StadiumOrArena", const=True, alias='@type')
    

StadiumOrArena.update_forward_refs()
