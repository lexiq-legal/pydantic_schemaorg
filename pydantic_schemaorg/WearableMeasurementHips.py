from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementHips(WearableMeasurementTypeEnumeration):
    """Measurement of the hip section, for example of a skirt

    See https://schema.org/WearableMeasurementHips.

    """
    type_: str = Field("WearableMeasurementHips", const=True, alias='@type')
    

WearableMeasurementHips.update_forward_refs()
