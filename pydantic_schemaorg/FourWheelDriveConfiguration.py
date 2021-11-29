from pydantic import Field
from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class FourWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Four-wheel drive is a transmission layout where the engine primarily drives two wheels"
     "with a part-time four-wheel drive capability.

    See https://schema.org/FourWheelDriveConfiguration.

    """

    locals().update({"@type": Field("FourWheelDriveConfiguration", const=True)})


FourWheelDriveConfiguration.update_forward_refs()
