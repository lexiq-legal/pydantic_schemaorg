from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class RentalVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle as a rental car.

    See https://schema.org/RentalVehicleUsage.

    """

    locals().update({"@type": Field("RentalVehicleUsage", const=True)})


RentalVehicleUsage.update_forward_refs()
