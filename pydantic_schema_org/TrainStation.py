from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class TrainStation(CivicStructure):
    """A train station.

    See https://schema.org/TrainStation.

    """

    locals().update({"@type": Field("TrainStation", const=True)})


TrainStation.update_forward_refs()
