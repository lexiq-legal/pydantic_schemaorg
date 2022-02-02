from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting"
     "of clothes.

    See: https://schema.org/BodyMeasurementTypeEnumeration
    Model depth: 5
    """
    type_: str = Field("BodyMeasurementTypeEnumeration", alias='@type')
    

