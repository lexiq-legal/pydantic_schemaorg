from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementBack(WearableMeasurementTypeEnumeration):
    """Measurement of the back section, for example of a jacket

    See https://schema.org/WearableMeasurementBack.

    """
    type_: str = Field("WearableMeasurementBack", const=True, alias='@type')
    

WearableMeasurementBack.update_forward_refs()
