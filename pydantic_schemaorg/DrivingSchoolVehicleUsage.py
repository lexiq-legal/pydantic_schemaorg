from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CarUsageType import CarUsageType


class DrivingSchoolVehicleUsage(CarUsageType):
    """Indicates the usage of the vehicle for driving school.

    See: https://schema.org/DrivingSchoolVehicleUsage
    Model depth: 5
    """

    type_: str = Field("DrivingSchoolVehicleUsage", const=True, alias="@type")


if TYPE_CHECKING:

    DrivingSchoolVehicleUsage.update_forward_refs()
