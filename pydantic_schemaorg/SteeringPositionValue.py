from pydantic import Field
from pydantic_schemaorg.QualitativeValue import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """A value indicating a steering position.

    See https://schema.org/SteeringPositionValue.

    """
    type_: str = Field("SteeringPositionValue", const=True, alias='@type')
    

SteeringPositionValue.update_forward_refs()
