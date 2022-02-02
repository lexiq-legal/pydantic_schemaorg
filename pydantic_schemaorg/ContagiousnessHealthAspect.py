from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ContagiousnessHealthAspect(HealthAspectEnumeration):
    """Content about contagion mechanisms and contagiousness information over the topic.

    See: https://schema.org/ContagiousnessHealthAspect
    Model depth: 5
    """
    type_: str = Field("ContagiousnessHealthAspect", alias='@type')
    

