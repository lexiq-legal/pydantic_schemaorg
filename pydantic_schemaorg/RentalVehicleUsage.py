from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class RentalVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle as a rental car.

    See https://schema.org/RentalVehicleUsage.

    """
    type_: str = Field("RentalVehicleUsage", const=True, alias='@type')
    

RentalVehicleUsage.update_forward_refs()
