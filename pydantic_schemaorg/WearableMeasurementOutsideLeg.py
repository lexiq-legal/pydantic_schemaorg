from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementOutsideLeg(WearableMeasurementTypeEnumeration):
    """Measurement of the outside leg, for example of pants

    See https://schema.org/WearableMeasurementOutsideLeg.

    """
    type_: str = Field("WearableMeasurementOutsideLeg", const=True, alias='@type')
    

WearableMeasurementOutsideLeg.update_forward_refs()
