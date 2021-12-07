from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility.

    See https://schema.org/ParkingFacility.

    """
    type_: str = Field("ParkingFacility", const=True, alias='@type')
    

ParkingFacility.update_forward_refs()
