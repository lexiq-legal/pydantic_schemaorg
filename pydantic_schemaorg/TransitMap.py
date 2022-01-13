from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MapCategoryType import MapCategoryType


class TransitMap(MapCategoryType):
    """A transit map.

    See: https://schema.org/TransitMap
    Model depth: 5
    """

    type_: str = Field("TransitMap", const=True, alias="@type")


if TYPE_CHECKING:

    TransitMap.update_forward_refs()
