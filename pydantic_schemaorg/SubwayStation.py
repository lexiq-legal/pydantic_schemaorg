from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class SubwayStation(CivicStructure):
    """A subway station.

    See https://schema.org/SubwayStation.

    """
    type_: str = Field("SubwayStation", const=True, alias='@type')
    

SubwayStation.update_forward_refs()
