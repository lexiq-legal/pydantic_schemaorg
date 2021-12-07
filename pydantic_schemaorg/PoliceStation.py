from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EmergencyService import EmergencyService


class PoliceStation(CivicStructure, EmergencyService):
    """A police station.

    See https://schema.org/PoliceStation.

    """
    type_: str = Field("PoliceStation", const=True, alias='@type')
    

PoliceStation.update_forward_refs()
