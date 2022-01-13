from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class BusStop(CivicStructure):
    """A bus stop.

    See: https://schema.org/BusStop
    Model depth: 4
    """

    type_: str = Field("BusStop", const=True, alias="@type")


if TYPE_CHECKING:

    BusStop.update_forward_refs()
