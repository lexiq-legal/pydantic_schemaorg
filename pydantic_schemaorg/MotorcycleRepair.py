from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop.

    See: https://schema.org/MotorcycleRepair
    Model depth: 5
    """

    type_: str = Field("MotorcycleRepair", const=True, alias="@type")


if TYPE_CHECKING:

    MotorcycleRepair.update_forward_refs()
