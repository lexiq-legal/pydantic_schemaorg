from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementUnderbust(BodyMeasurementTypeEnumeration):
    """Girth of body just below the bust. Used, for example, to fit women's swimwear.

    See: https://schema.org/BodyMeasurementUnderbust
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementUnderbust", alias='@type')
    

