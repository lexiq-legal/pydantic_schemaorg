from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHips(BodyMeasurementTypeEnumeration):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    See https://schema.org/BodyMeasurementHips.

    """
    type_: str = Field("BodyMeasurementHips", const=True, alias='@type')
    

BodyMeasurementHips.update_forward_refs()
