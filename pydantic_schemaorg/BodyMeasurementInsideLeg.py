from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementInsideLeg(BodyMeasurementTypeEnumeration):
    """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

    See: https://schema.org/BodyMeasurementInsideLeg
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementInsideLeg", alias='@type')
    

