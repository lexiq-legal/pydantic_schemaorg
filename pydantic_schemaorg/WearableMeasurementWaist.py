from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementWaist(WearableMeasurementTypeEnumeration):
    """Measurement of the waist section, for example of pants

    See: https://schema.org/WearableMeasurementWaist
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementWaist", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementWaist.update_forward_refs()
