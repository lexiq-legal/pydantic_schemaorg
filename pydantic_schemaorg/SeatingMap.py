from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MapCategoryType import MapCategoryType


class SeatingMap(MapCategoryType):
    """A seating map.

    See: https://schema.org/SeatingMap
    Model depth: 5
    """

    type_: str = Field("SeatingMap", const=True, alias="@type")


if TYPE_CHECKING:

    SeatingMap.update_forward_refs()
