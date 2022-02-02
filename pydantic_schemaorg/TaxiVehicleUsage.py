from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class TaxiVehicleUsage(CarUsageType):
    """Indicates the usage of the car as a taxi.

    See: https://schema.org/TaxiVehicleUsage
    Model depth: 5
    """
    type_: str = Field("TaxiVehicleUsage", alias='@type')
    

