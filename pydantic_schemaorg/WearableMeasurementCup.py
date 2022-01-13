from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementCup(WearableMeasurementTypeEnumeration):
    """Measurement of the cup, for example of a bra

    See: https://schema.org/WearableMeasurementCup
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementCup", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementCup.update_forward_refs()
