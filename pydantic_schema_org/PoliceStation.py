from pydantic import Field
from pydantic_schema_org.EmergencyService import EmergencyService
from pydantic_schema_org.CivicStructure import CivicStructure


class PoliceStation(EmergencyService, CivicStructure):
    """A police station.

    See https://schema.org/PoliceStation.

    """

    locals().update({"@type": Field("PoliceStation", const=True)})


PoliceStation.update_forward_refs()
