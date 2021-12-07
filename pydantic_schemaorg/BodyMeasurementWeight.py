from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementWeight(BodyMeasurementTypeEnumeration):
    """Body weight. Used, for example, to measure pantyhose.

    See https://schema.org/BodyMeasurementWeight.

    """
    type_: str = Field("BodyMeasurementWeight", const=True, alias='@type')
    

BodyMeasurementWeight.update_forward_refs()
