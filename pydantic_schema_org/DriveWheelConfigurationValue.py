from pydantic import Field
from pydantic_schema_org.QualitativeValue import QualitativeValue


class DriveWheelConfigurationValue(QualitativeValue):
    """A value indicating which roadwheels will receive torque.

    See https://schema.org/DriveWheelConfigurationValue.

    """

    locals().update({"@type": Field("DriveWheelConfigurationValue", const=True)})


DriveWheelConfigurationValue.update_forward_refs()
