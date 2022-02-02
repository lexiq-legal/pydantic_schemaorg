from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementBack(WearableMeasurementTypeEnumeration):
    """Measurement of the back section, for example of a jacket

    See: https://schema.org/WearableMeasurementBack
    Model depth: 6
    """
    type_: str = Field("WearableMeasurementBack", alias='@type')
    

