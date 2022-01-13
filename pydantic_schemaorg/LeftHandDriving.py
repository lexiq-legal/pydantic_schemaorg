from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SteeringPositionValue import SteeringPositionValue


class LeftHandDriving(SteeringPositionValue):
    """The steering position is on the left side of the vehicle (viewed from the main direction"
     "of driving).

    See: https://schema.org/LeftHandDriving
    Model depth: 6
    """

    type_: str = Field("LeftHandDriving", const=True, alias="@type")


if TYPE_CHECKING:

    LeftHandDriving.update_forward_refs()
