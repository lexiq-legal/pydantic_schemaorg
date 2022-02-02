from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ScreeningHealthAspect(HealthAspectEnumeration):
    """Content about how to screen or further filter a topic.

    See: https://schema.org/ScreeningHealthAspect
    Model depth: 5
    """
    type_: str = Field("ScreeningHealthAspect", alias='@type')
    

