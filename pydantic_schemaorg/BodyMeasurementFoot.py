from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementFoot(BodyMeasurementTypeEnumeration):
    """Foot length (measured between end of the most prominent toe and the most prominent part"
     "of the heel). Used, for example, to measure socks.

    See: https://schema.org/BodyMeasurementFoot
    Model depth: 6
    """

    type_: str = Field("BodyMeasurementFoot", const=True, alias="@type")


if TYPE_CHECKING:

    BodyMeasurementFoot.update_forward_refs()
