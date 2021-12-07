from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class RearWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Real-wheel drive is a transmission layout where the engine drives the rear wheels.

    See https://schema.org/RearWheelDriveConfiguration.

    """
    type_: str = Field("RearWheelDriveConfiguration", const=True, alias='@type')
    

RearWheelDriveConfiguration.update_forward_refs()
