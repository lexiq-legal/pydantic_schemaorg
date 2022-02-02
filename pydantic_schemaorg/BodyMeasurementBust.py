from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementBust(BodyMeasurementTypeEnumeration):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    See: https://schema.org/BodyMeasurementBust
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementBust", alias='@type')
    

