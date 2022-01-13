from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.QualitativeValue import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """A value indicating a steering position.

    See: https://schema.org/SteeringPositionValue
    Model depth: 5
    """

    type_: str = Field("SteeringPositionValue", const=True, alias="@type")


if TYPE_CHECKING:

    SteeringPositionValue.update_forward_refs()
