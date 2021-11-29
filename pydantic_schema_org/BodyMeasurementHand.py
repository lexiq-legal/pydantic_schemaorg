from pydantic import Field
from pydantic_schema_org.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHand(BodyMeasurementTypeEnumeration):
    """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb,"
     "fingers together). Used, for example, to fit gloves.

    See https://schema.org/BodyMeasurementHand.

    """

    locals().update({"@type": Field("BodyMeasurementHand", const=True)})


BodyMeasurementHand.update_forward_refs()
