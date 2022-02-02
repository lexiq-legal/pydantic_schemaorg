from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SideEffectsHealthAspect(HealthAspectEnumeration):
    """Side effects that can be observed from the usage of the topic.

    See: https://schema.org/SideEffectsHealthAspect
    Model depth: 5
    """
    type_: str = Field("SideEffectsHealthAspect", alias='@type')
    

