from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class AllWheelDriveConfiguration(DriveWheelConfigurationValue):
    """All-wheel Drive is a transmission layout where the engine drives all four wheels.

    See https://schema.org/AllWheelDriveConfiguration.

    """
    type_: str = Field("AllWheelDriveConfiguration", const=True, alias='@type')
    

AllWheelDriveConfiguration.update_forward_refs()
