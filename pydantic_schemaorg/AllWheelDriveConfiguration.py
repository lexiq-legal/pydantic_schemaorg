from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class AllWheelDriveConfiguration(DriveWheelConfigurationValue):
    """All-wheel Drive is a transmission layout where the engine drives all four wheels.

    See: https://schema.org/AllWheelDriveConfiguration
    Model depth: 6
    """
    type_: str = Field("AllWheelDriveConfiguration", alias='@type')
    

