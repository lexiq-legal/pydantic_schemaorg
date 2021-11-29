from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementInsideLeg(BodyMeasurementTypeEnumeration):
    """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

    See https://schema.org/BodyMeasurementInsideLeg.

    """

    locals().update({"@type": Field("BodyMeasurementInsideLeg", const=True)})


BodyMeasurementInsideLeg.update_forward_refs()
