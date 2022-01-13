from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EmergencyService import EmergencyService

from pydantic_schemaorg.CivicStructure import CivicStructure


class FireStation(EmergencyService, CivicStructure):
    """A fire station. With firemen.

    See: https://schema.org/FireStation
    Model depth: 4
    """

    type_: str = Field("FireStation", const=True, alias="@type")


if TYPE_CHECKING:

    FireStation.update_forward_refs()
