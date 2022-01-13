from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementLength(WearableMeasurementTypeEnumeration):
    """Represents the length, for example of a dress

    See: https://schema.org/WearableMeasurementLength
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementLength", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementLength.update_forward_refs()
