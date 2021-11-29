from pydantic import Field
from pydantic_schema_org.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class AllWheelDriveConfiguration(DriveWheelConfigurationValue):
    """All-wheel Drive is a transmission layout where the engine drives all four wheels.

    See https://schema.org/AllWheelDriveConfiguration.

    """

    locals().update({"@type": Field("AllWheelDriveConfiguration", const=True)})


AllWheelDriveConfiguration.update_forward_refs()
