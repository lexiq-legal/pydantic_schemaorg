from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementWeight(BodyMeasurementTypeEnumeration):
    """Body weight. Used, for example, to measure pantyhose.

    See: https://schema.org/BodyMeasurementWeight
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementWeight", alias='@type')
    

