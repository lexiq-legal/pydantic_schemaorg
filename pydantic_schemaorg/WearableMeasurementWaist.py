from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementWaist(WearableMeasurementTypeEnumeration):
    """Measurement of the waist section, for example of pants

    See https://schema.org/WearableMeasurementWaist.

    """
    type_: str = Field("WearableMeasurementWaist", const=True, alias='@type')
    

WearableMeasurementWaist.update_forward_refs()
