from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class FrontWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Front-wheel drive is a transmission layout where the engine drives the front wheels.

    See https://schema.org/FrontWheelDriveConfiguration.

    """
    type_: str = Field("FrontWheelDriveConfiguration", const=True, alias='@type')
    

FrontWheelDriveConfiguration.update_forward_refs()
