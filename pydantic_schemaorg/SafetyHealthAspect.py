from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SafetyHealthAspect(HealthAspectEnumeration):
    """Content about the safety-related aspects of a health topic.

    See: https://schema.org/SafetyHealthAspect
    Model depth: 5
    """
    type_: str = Field("SafetyHealthAspect", alias='@type')
    

