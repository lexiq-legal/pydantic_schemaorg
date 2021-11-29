from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class FrontWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Front-wheel drive is a transmission layout where the engine drives the front wheels.

    See https://schema.org/FrontWheelDriveConfiguration.

    """

    locals().update({"@type": Field("FrontWheelDriveConfiguration", const=True)})


FrontWheelDriveConfiguration.update_forward_refs()
