from pydantic import Field
from pydantic_schemaorg.SteeringPositionValue import SteeringPositionValue


class LeftHandDriving(SteeringPositionValue):
    """The steering position is on the left side of the vehicle (viewed from the main direction"
     "of driving).

    See https://schema.org/LeftHandDriving.

    """

    locals().update({"@type": Field("LeftHandDriving", const=True)})


LeftHandDriving.update_forward_refs()
