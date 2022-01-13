from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MapCategoryType import MapCategoryType


class VenueMap(MapCategoryType):
    """A venue map (e.g. for malls, auditoriums, museums, etc.).

    See: https://schema.org/VenueMap
    Model depth: 5
    """

    type_: str = Field("VenueMap", const=True, alias="@type")


if TYPE_CHECKING:

    VenueMap.update_forward_refs()
