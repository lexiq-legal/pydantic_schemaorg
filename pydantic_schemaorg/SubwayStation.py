from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class SubwayStation(CivicStructure):
    """A subway station.

    See https://schema.org/SubwayStation.

    """

    locals().update({"@type": Field("SubwayStation", const=True)})


SubwayStation.update_forward_refs()
