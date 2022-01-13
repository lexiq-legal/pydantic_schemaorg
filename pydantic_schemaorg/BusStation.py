from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStation(CivicStructure):
    """A bus station.

    See: https://schema.org/BusStation
    Model depth: 4
    """

    type_: str = Field("BusStation", const=True, alias="@type")


if TYPE_CHECKING:

    BusStation.update_forward_refs()
