from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class StagesHealthAspect(HealthAspectEnumeration):
    """Stages that can be observed from a topic.

    See: https://schema.org/StagesHealthAspect
    Model depth: 5
    """
    type_: str = Field("StagesHealthAspect", alias='@type')
    

