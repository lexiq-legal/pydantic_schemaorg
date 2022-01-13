from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Place import Place


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building.

    See: https://schema.org/LandmarksOrHistoricalBuildings
    Model depth: 3
    """

    type_: str = Field("LandmarksOrHistoricalBuildings", const=True, alias="@type")


if TYPE_CHECKING:

    LandmarksOrHistoricalBuildings.update_forward_refs()
