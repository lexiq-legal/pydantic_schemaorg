from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class TrainStation(CivicStructure):
    """A train station.

    See: https://schema.org/TrainStation
    Model depth: 4
    """

    type_: str = Field("TrainStation", const=True, alias="@type")


if TYPE_CHECKING:

    TrainStation.update_forward_refs()
