from pydantic import Field
from pydantic_schemaorg.SteeringPositionValue import SteeringPositionValue


class RightHandDriving(SteeringPositionValue):
    """The steering position is on the right side of the vehicle (viewed from the main direction"
     "of driving).

    See https://schema.org/RightHandDriving.

    """

    locals().update({"@type": Field("RightHandDriving", const=True)})


RightHandDriving.update_forward_refs()
