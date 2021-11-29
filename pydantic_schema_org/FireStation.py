from pydantic import Field
from pydantic_schema_org.EmergencyService import EmergencyService
from pydantic_schema_org.CivicStructure import CivicStructure


class FireStation(EmergencyService, CivicStructure):
    """A fire station. With firemen.

    See https://schema.org/FireStation.

    """

    locals().update({"@type": Field("FireStation", const=True)})


FireStation.update_forward_refs()
