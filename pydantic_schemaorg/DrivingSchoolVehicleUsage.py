from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class DrivingSchoolVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle for driving school.

    See https://schema.org/DrivingSchoolVehicleUsage.

    """

    locals().update({"@type": Field("DrivingSchoolVehicleUsage", const=True)})


DrivingSchoolVehicleUsage.update_forward_refs()
