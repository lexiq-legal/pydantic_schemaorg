from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementInseam(WearableMeasurementTypeEnumeration):
    """Measurement of the inseam, for example of pants

    See: https://schema.org/WearableMeasurementInseam
    Model depth: 6
    """
    type_: str = Field("WearableMeasurementInseam", alias='@type')
    

