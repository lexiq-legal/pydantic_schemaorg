from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementHips(BodyMeasurementTypeEnumeration):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    See: https://schema.org/BodyMeasurementHips
    Model depth: 6
    """

    type_: str = Field("BodyMeasurementHips", const=True, alias="@type")


if TYPE_CHECKING:

    BodyMeasurementHips.update_forward_refs()
