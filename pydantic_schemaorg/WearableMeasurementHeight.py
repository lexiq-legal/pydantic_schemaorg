from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementHeight(WearableMeasurementTypeEnumeration):
    """Measurement of the height, for example the heel height of a shoe

    See https://schema.org/WearableMeasurementHeight.

    """
    type_: str = Field("WearableMeasurementHeight", const=True, alias='@type')
    

WearableMeasurementHeight.update_forward_refs()
