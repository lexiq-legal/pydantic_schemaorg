from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.QualitativeValue import QualitativeValue


class DriveWheelConfigurationValue(QualitativeValue):
    """A value indicating which roadwheels will receive torque.

    See: https://schema.org/DriveWheelConfigurationValue
    Model depth: 5
    """
    type_: str = Field("DriveWheelConfigurationValue", alias='@type')
    

