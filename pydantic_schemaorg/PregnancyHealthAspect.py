from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PregnancyHealthAspect(HealthAspectEnumeration):
    """Content discussing pregnancy-related aspects of a health topic.

    See: https://schema.org/PregnancyHealthAspect
    Model depth: 5
    """
    type_: str = Field("PregnancyHealthAspect", alias='@type')
    

