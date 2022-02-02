from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class ParkingMap(MapCategoryType):
    """A parking map.

    See: https://schema.org/ParkingMap
    Model depth: 5
    """
    type_: str = Field("ParkingMap", alias='@type')
    

