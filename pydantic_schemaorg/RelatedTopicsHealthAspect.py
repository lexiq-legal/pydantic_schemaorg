from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RelatedTopicsHealthAspect(HealthAspectEnumeration):
    """Other prominent or relevant topics tied to the main topic.

    See: https://schema.org/RelatedTopicsHealthAspect
    Model depth: 5
    """
    type_: str = Field("RelatedTopicsHealthAspect", alias='@type')
    

