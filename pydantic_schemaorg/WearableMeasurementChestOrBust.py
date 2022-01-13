from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementChestOrBust(WearableMeasurementTypeEnumeration):
    """Measurement of the chest/bust section, for example of a suit

    See: https://schema.org/WearableMeasurementChestOrBust
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementChestOrBust", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementChestOrBust.update_forward_refs()
