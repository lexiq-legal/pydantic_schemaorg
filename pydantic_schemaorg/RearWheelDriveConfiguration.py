from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class RearWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Real-wheel drive is a transmission layout where the engine drives the rear wheels.

    See: https://schema.org/RearWheelDriveConfiguration
    Model depth: 6
    """

    type_: str = Field("RearWheelDriveConfiguration", const=True, alias="@type")


if TYPE_CHECKING:

    RearWheelDriveConfiguration.update_forward_refs()
