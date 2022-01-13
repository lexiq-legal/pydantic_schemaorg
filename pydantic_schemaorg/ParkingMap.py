from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MapCategoryType import MapCategoryType


class ParkingMap(MapCategoryType):
    """A parking map.

    See: https://schema.org/ParkingMap
    Model depth: 5
    """

    type_: str = Field("ParkingMap", const=True, alias="@type")


if TYPE_CHECKING:

    ParkingMap.update_forward_refs()
