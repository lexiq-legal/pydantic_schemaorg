from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementHeight(BodyMeasurementTypeEnumeration):
    """Body height (measured between crown of head and soles of feet). Used, for example, to"
     "fit jackets.

    See: https://schema.org/BodyMeasurementHeight
    Model depth: 6
    """

    type_: str = Field("BodyMeasurementHeight", const=True, alias="@type")


if TYPE_CHECKING:

    BodyMeasurementHeight.update_forward_refs()
