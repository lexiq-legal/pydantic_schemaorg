from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementChest(BodyMeasurementTypeEnumeration):
    """Maximum girth of chest. Used, for example, to fit men's suits.

    See https://schema.org/BodyMeasurementChest.

    """
    type_: str = Field("BodyMeasurementChest", const=True, alias='@type')
    

BodyMeasurementChest.update_forward_refs()
