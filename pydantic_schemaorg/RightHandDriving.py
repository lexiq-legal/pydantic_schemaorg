from pydantic import Field
from pydantic_schemaorg.SteeringPositionValue import SteeringPositionValue


class RightHandDriving(SteeringPositionValue):
    """The steering position is on the right side of the vehicle (viewed from the main direction"
     "of driving).

    See https://schema.org/RightHandDriving.

    """
    type_: str = Field("RightHandDriving", const=True, alias='@type')
    

RightHandDriving.update_forward_refs()
