from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting"
     "of clothes.

    See: https://schema.org/BodyMeasurementTypeEnumeration
    Model depth: 5
    """

    type_: str = Field("BodyMeasurementTypeEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    BodyMeasurementTypeEnumeration.update_forward_refs()
