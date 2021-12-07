from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStop(CivicStructure):
    """A bus stop.

    See https://schema.org/BusStop.

    """
    type_: str = Field("BusStop", const=True, alias='@type')
    

BusStop.update_forward_refs()
