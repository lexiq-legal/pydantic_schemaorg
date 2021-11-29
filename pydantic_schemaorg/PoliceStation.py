from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EmergencyService import EmergencyService


class PoliceStation(CivicStructure, EmergencyService):
    """A police station.

    See https://schema.org/PoliceStation.

    """

    locals().update({"@type": Field("PoliceStation", const=True)})


PoliceStation.update_forward_refs()
