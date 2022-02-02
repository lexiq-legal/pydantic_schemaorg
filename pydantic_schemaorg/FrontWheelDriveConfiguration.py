from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class FrontWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Front-wheel drive is a transmission layout where the engine drives the front wheels.

    See: https://schema.org/FrontWheelDriveConfiguration
    Model depth: 6
    """
    type_: str = Field("FrontWheelDriveConfiguration", alias='@type')
    

