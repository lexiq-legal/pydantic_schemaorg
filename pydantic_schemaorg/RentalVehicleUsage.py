from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class RentalVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle as a rental car.

    See: https://schema.org/RentalVehicleUsage
    Model depth: 5
    """
    type_: str = Field("RentalVehicleUsage", alias='@type')
    

