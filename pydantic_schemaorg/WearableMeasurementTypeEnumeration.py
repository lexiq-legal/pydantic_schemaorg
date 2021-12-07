from pydantic import Field
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates common types of measurement for wearables products.

    See https://schema.org/WearableMeasurementTypeEnumeration.

    """
    type_: str = Field("WearableMeasurementTypeEnumeration", const=True, alias='@type')
    

WearableMeasurementTypeEnumeration.update_forward_refs()
