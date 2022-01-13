from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementHips(WearableMeasurementTypeEnumeration):
    """Measurement of the hip section, for example of a skirt

    See: https://schema.org/WearableMeasurementHips
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementHips", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementHips.update_forward_refs()
