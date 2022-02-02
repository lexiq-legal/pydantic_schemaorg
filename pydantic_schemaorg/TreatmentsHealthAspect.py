from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TreatmentsHealthAspect(HealthAspectEnumeration):
    """Treatments or related therapies for a Topic.

    See: https://schema.org/TreatmentsHealthAspect
    Model depth: 5
    """
    type_: str = Field("TreatmentsHealthAspect", alias='@type')
    

