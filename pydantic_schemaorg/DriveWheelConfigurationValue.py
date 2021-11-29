from pydantic import Field
from pydantic_schemaorg.QualitativeValue import QualitativeValue


class DriveWheelConfigurationValue(QualitativeValue):
    """A value indicating which roadwheels will receive torque.

    See https://schema.org/DriveWheelConfigurationValue.

    """

    locals().update({"@type": Field("DriveWheelConfigurationValue", const=True)})


DriveWheelConfigurationValue.update_forward_refs()
