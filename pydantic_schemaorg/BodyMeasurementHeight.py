from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHeight(BodyMeasurementTypeEnumeration):
    """Body height (measured between crown of head and soles of feet). Used, for example, to"
     "fit jackets.

    See https://schema.org/BodyMeasurementHeight.

    """
    type_: str = Field("BodyMeasurementHeight", const=True, alias='@type')
    

BodyMeasurementHeight.update_forward_refs()
