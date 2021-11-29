from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class TaxiVehicleUsage(CarUsageType):
    """Indicates the usage of the car as a taxi.

    See https://schema.org/TaxiVehicleUsage.

    """

    locals().update({"@type": Field("TaxiVehicleUsage", const=True)})


TaxiVehicleUsage.update_forward_refs()
