from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class LivingWithHealthAspect(HealthAspectEnumeration):
    """Information about coping or life related to the topic.

    See: https://schema.org/LivingWithHealthAspect
    Model depth: 5
    """
    type_: str = Field("LivingWithHealthAspect", alias='@type')
    

