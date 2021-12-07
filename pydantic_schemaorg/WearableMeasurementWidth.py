from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementWidth(WearableMeasurementTypeEnumeration):
    """Measurement of the width, for example of shoes

    See https://schema.org/WearableMeasurementWidth.

    """
    type_: str = Field("WearableMeasurementWidth", const=True, alias='@type')
    

WearableMeasurementWidth.update_forward_refs()
