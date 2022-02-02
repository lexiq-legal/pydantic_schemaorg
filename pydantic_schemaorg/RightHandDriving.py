from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SteeringPositionValue import SteeringPositionValue


class RightHandDriving(SteeringPositionValue):
    """The steering position is on the right side of the vehicle (viewed from the main direction"
     "of driving).

    See: https://schema.org/RightHandDriving
    Model depth: 6
    """
    type_: str = Field("RightHandDriving", alias='@type')
    

