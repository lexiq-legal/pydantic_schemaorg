from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility.

    See: https://schema.org/ParkingFacility
    Model depth: 4
    """
    type_: str = Field("ParkingFacility", alias='@type')
    

