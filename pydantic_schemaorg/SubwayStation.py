from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class SubwayStation(CivicStructure):
    """A subway station.

    See: https://schema.org/SubwayStation
    Model depth: 4
    """

    type_: str = Field("SubwayStation", const=True, alias="@type")


if TYPE_CHECKING:

    SubwayStation.update_forward_refs()
