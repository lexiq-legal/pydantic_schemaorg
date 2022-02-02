from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates common types of measurement for wearables products.

    See: https://schema.org/WearableMeasurementTypeEnumeration
    Model depth: 5
    """
    type_: str = Field("WearableMeasurementTypeEnumeration", alias='@type')
    

