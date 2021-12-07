from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementCup(WearableMeasurementTypeEnumeration):
    """Measurement of the cup, for example of a bra

    See https://schema.org/WearableMeasurementCup.

    """
    type_: str = Field("WearableMeasurementCup", const=True, alias='@type')
    

WearableMeasurementCup.update_forward_refs()
