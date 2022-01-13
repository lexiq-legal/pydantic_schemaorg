from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates common types of measurement for wearables products.

    See: https://schema.org/WearableMeasurementTypeEnumeration
    Model depth: 5
    """

    type_: str = Field("WearableMeasurementTypeEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementTypeEnumeration.update_forward_refs()
