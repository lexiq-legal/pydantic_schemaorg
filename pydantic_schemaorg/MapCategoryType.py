from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class MapCategoryType(Enumeration):
    """An enumeration of several kinds of Map.

    See: https://schema.org/MapCategoryType
    Model depth: 4
    """

    type_: str = Field("MapCategoryType", const=True, alias="@type")


if TYPE_CHECKING:

    MapCategoryType.update_forward_refs()
