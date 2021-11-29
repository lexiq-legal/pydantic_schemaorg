from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EmergencyService import EmergencyService


class FireStation(CivicStructure, EmergencyService):
    """A fire station. With firemen.

    See https://schema.org/FireStation.

    """

    locals().update({"@type": Field("FireStation", const=True)})


FireStation.update_forward_refs()
