from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStation(CivicStructure):
    """A bus station.

    See https://schema.org/BusStation.

    """

    locals().update({"@type": Field("BusStation", const=True)})


BusStation.update_forward_refs()
