from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EmergencyService import EmergencyService

from pydantic_schemaorg.CivicStructure import CivicStructure


class PoliceStation(EmergencyService, CivicStructure):
    """A police station.

    See: https://schema.org/PoliceStation
    Model depth: 4
    """

    type_: str = Field("PoliceStation", const=True, alias="@type")


if TYPE_CHECKING:

    PoliceStation.update_forward_refs()
