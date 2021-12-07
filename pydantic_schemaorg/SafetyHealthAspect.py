from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SafetyHealthAspect(HealthAspectEnumeration):
    """Content about the safety-related aspects of a health topic.

    See https://schema.org/SafetyHealthAspect.

    """
    type_: str = Field("SafetyHealthAspect", const=True, alias='@type')
    

SafetyHealthAspect.update_forward_refs()
