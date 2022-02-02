from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class MayTreatHealthAspect(HealthAspectEnumeration):
    """Related topics may be treated by a Topic.

    See: https://schema.org/MayTreatHealthAspect
    Model depth: 5
    """
    type_: str = Field("MayTreatHealthAspect", alias='@type')
    

