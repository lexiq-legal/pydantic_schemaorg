from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.QualitativeValue import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """A value indicating a steering position.

    See: https://schema.org/SteeringPositionValue
    Model depth: 5
    """
    type_: str = Field("SteeringPositionValue", alias='@type')
    

