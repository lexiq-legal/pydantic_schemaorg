from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementHeight(WearableMeasurementTypeEnumeration):
    """Measurement of the height, for example the heel height of a shoe

    See: https://schema.org/WearableMeasurementHeight
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementHeight", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementHeight.update_forward_refs()
