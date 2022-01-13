from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementCollar(WearableMeasurementTypeEnumeration):
    """Measurement of the collar, for example of a shirt

    See: https://schema.org/WearableMeasurementCollar
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementCollar", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementCollar.update_forward_refs()
