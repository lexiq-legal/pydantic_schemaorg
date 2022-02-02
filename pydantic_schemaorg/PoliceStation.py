from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EmergencyService import EmergencyService
from pydantic_schemaorg.CivicStructure import CivicStructure


class PoliceStation(EmergencyService, CivicStructure):
    """A police station.

    See: https://schema.org/PoliceStation
    Model depth: 4
    """
    type_: str = Field("PoliceStation", alias='@type')
    

