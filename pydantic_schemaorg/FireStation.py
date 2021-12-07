from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EmergencyService import EmergencyService


class FireStation(CivicStructure, EmergencyService):
    """A fire station. With firemen.

    See https://schema.org/FireStation.

    """
    type_: str = Field("FireStation", const=True, alias='@type')
    

FireStation.update_forward_refs()
