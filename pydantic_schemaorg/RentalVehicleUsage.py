from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CarUsageType import CarUsageType


class RentalVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle as a rental car.

    See: https://schema.org/RentalVehicleUsage
    Model depth: 5
    """

    type_: str = Field("RentalVehicleUsage", const=True, alias="@type")


if TYPE_CHECKING:

    RentalVehicleUsage.update_forward_refs()
