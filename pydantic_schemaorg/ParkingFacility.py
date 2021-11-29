from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility.

    See https://schema.org/ParkingFacility.

    """

    locals().update({"@type": Field("ParkingFacility", const=True)})


ParkingFacility.update_forward_refs()
