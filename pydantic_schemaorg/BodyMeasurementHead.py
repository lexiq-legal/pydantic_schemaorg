from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHead(BodyMeasurementTypeEnumeration):
    """Maximum girth of head above the ears. Used, for example, to fit hats.

    See https://schema.org/BodyMeasurementHead.

    """
    type_: str = Field("BodyMeasurementHead", const=True, alias='@type')
    

BodyMeasurementHead.update_forward_refs()
