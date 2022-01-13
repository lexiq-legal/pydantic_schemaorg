from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """A gas station.

    See: https://schema.org/GasStation
    Model depth: 5
    """

    type_: str = Field("GasStation", const=True, alias="@type")


if TYPE_CHECKING:

    GasStation.update_forward_refs()
