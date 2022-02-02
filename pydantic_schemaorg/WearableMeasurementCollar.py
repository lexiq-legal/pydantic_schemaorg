from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementCollar(WearableMeasurementTypeEnumeration):
    """Measurement of the collar, for example of a shirt

    See: https://schema.org/WearableMeasurementCollar
    Model depth: 6
    """
    type_: str = Field("WearableMeasurementCollar", alias='@type')
    

