from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SymptomsHealthAspect(HealthAspectEnumeration):
    """Symptoms or related symptoms of a Topic.

    See: https://schema.org/SymptomsHealthAspect
    Model depth: 5
    """
    type_: str = Field("SymptomsHealthAspect", alias='@type')
    

