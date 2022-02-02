from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class CausesHealthAspect(HealthAspectEnumeration):
    """Information about the causes and main actions that gave rise to the topic.

    See: https://schema.org/CausesHealthAspect
    Model depth: 5
    """
    type_: str = Field("CausesHealthAspect", alias='@type')
    

