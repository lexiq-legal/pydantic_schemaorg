from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementInseam(WearableMeasurementTypeEnumeration):
    """Measurement of the inseam, for example of pants

    See: https://schema.org/WearableMeasurementInseam
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementInseam", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementInseam.update_forward_refs()
