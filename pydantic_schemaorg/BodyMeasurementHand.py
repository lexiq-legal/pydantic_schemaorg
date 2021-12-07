from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHand(BodyMeasurementTypeEnumeration):
    """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb,"
     "fingers together). Used, for example, to fit gloves.

    See https://schema.org/BodyMeasurementHand.

    """
    type_: str = Field("BodyMeasurementHand", const=True, alias='@type')
    

BodyMeasurementHand.update_forward_refs()
