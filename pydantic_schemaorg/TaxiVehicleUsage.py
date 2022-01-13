from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CarUsageType import CarUsageType


class TaxiVehicleUsage(CarUsageType):
    """Indicates the usage of the car as a taxi.

    See: https://schema.org/TaxiVehicleUsage
    Model depth: 5
    """

    type_: str = Field("TaxiVehicleUsage", const=True, alias="@type")


if TYPE_CHECKING:

    TaxiVehicleUsage.update_forward_refs()
