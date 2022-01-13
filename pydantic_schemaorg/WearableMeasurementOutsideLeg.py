from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementOutsideLeg(WearableMeasurementTypeEnumeration):
    """Measurement of the outside leg, for example of pants

    See: https://schema.org/WearableMeasurementOutsideLeg
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementOutsideLeg", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementOutsideLeg.update_forward_refs()
