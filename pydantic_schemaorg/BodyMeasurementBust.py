from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementBust(BodyMeasurementTypeEnumeration):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    See https://schema.org/BodyMeasurementBust.

    """
    type_: str = Field("BodyMeasurementBust", const=True, alias='@type')
    

BodyMeasurementBust.update_forward_refs()
