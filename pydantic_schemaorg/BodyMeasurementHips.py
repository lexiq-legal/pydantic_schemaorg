from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHips(BodyMeasurementTypeEnumeration):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    See: https://schema.org/BodyMeasurementHips
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementHips", alias='@type')
    

