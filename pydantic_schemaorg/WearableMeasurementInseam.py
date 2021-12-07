from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementInseam(WearableMeasurementTypeEnumeration):
    """Measurement of the inseam, for example of pants

    See https://schema.org/WearableMeasurementInseam.

    """
    type_: str = Field("WearableMeasurementInseam", const=True, alias='@type')
    

WearableMeasurementInseam.update_forward_refs()
