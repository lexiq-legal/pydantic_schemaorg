from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class TaxiVehicleUsage(CarUsageType):
    """Indicates the usage of the car as a taxi.

    See https://schema.org/TaxiVehicleUsage.

    """
    type_: str = Field("TaxiVehicleUsage", const=True, alias='@type')
    

TaxiVehicleUsage.update_forward_refs()
