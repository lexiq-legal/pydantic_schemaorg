from pydantic import Field
from pydantic_schemaorg.QualitativeValue import QualitativeValue


class DriveWheelConfigurationValue(QualitativeValue):
    """A value indicating which roadwheels will receive torque.

    See https://schema.org/DriveWheelConfigurationValue.

    """
    type_: str = Field("DriveWheelConfigurationValue", const=True, alias='@type')
    

DriveWheelConfigurationValue.update_forward_refs()
