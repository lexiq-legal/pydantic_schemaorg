from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class ParkingMap(MapCategoryType):
    """A parking map.

    See https://schema.org/ParkingMap.

    """
    type_: str = Field("ParkingMap", const=True, alias='@type')
    

ParkingMap.update_forward_refs()
