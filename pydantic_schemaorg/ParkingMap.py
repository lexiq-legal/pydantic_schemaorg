from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class ParkingMap(MapCategoryType):
    """A parking map.

    See https://schema.org/ParkingMap.

    """

    locals().update({"@type": Field("ParkingMap", const=True)})


ParkingMap.update_forward_refs()
