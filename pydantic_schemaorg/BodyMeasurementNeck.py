from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementNeck(BodyMeasurementTypeEnumeration):
    """Girth of neck. Used, for example, to fit shirts.

    See: https://schema.org/BodyMeasurementNeck
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementNeck", alias='@type')
    

