from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementWidth(WearableMeasurementTypeEnumeration):
    """Measurement of the width, for example of shoes

    See: https://schema.org/WearableMeasurementWidth
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementWidth", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementWidth.update_forward_refs()
