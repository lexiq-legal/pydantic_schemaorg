from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHeight(BodyMeasurementTypeEnumeration):
    """Body height (measured between crown of head and soles of feet). Used, for example, to"
     "fit jackets.

    See: https://schema.org/BodyMeasurementHeight
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementHeight", alias='@type')
    

