from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHand(BodyMeasurementTypeEnumeration):
    """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb,"
     "fingers together). Used, for example, to fit gloves.

    See: https://schema.org/BodyMeasurementHand
    Model depth: 6
    """
    type_: str = Field("BodyMeasurementHand", alias='@type')
    

