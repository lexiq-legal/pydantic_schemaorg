from pydantic import Field
from pydantic_schemaorg.Place import Place


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building.

    See https://schema.org/LandmarksOrHistoricalBuildings.

    """
    type_: str = Field("LandmarksOrHistoricalBuildings", const=True, alias='@type')
    

LandmarksOrHistoricalBuildings.update_forward_refs()
