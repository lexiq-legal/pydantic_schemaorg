from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableMeasurementTypeEnumeration import (
    WearableMeasurementTypeEnumeration,
)


class WearableMeasurementBack(WearableMeasurementTypeEnumeration):
    """Measurement of the back section, for example of a jacket

    See: https://schema.org/WearableMeasurementBack
    Model depth: 6
    """

    type_: str = Field("WearableMeasurementBack", const=True, alias="@type")


if TYPE_CHECKING:

    WearableMeasurementBack.update_forward_refs()
