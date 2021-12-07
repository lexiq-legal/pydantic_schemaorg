from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStation(CivicStructure):
    """A bus station.

    See https://schema.org/BusStation.

    """
    type_: str = Field("BusStation", const=True, alias='@type')
    

BusStation.update_forward_refs()
