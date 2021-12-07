from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class AllergiesHealthAspect(HealthAspectEnumeration):
    """Content about the allergy-related aspects of a health topic.

    See https://schema.org/AllergiesHealthAspect.

    """
    type_: str = Field("AllergiesHealthAspect", const=True, alias='@type')
    

AllergiesHealthAspect.update_forward_refs()
