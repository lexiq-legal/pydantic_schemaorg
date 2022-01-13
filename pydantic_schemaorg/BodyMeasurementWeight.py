from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementWeight(BodyMeasurementTypeEnumeration):
    """Body weight. Used, for example, to measure pantyhose.

    See: https://schema.org/BodyMeasurementWeight
    Model depth: 6
    """

    type_: str = Field("BodyMeasurementWeight", const=True, alias="@type")


if TYPE_CHECKING:

    BodyMeasurementWeight.update_forward_refs()
