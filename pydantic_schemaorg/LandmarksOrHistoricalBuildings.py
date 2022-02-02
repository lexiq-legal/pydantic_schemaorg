from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Place import Place


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building.

    See: https://schema.org/LandmarksOrHistoricalBuildings
    Model depth: 3
    """
    type_: str = Field("LandmarksOrHistoricalBuildings", alias='@type')
    

