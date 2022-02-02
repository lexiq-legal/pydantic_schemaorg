from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CarUsageType import CarUsageType


class DrivingSchoolVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle for driving school.

    See: https://schema.org/DrivingSchoolVehicleUsage
    Model depth: 5
    """
    type_: str = Field("DrivingSchoolVehicleUsage", alias='@type')
    

