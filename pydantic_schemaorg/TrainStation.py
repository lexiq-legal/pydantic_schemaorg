from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class TrainStation(CivicStructure):
    """A train station.

    See https://schema.org/TrainStation.

    """
    type_: str = Field("TrainStation", const=True, alias='@type')
    

TrainStation.update_forward_refs()
