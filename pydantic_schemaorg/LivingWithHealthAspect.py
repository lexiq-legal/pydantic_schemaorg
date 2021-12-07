from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class LivingWithHealthAspect(HealthAspectEnumeration):
    """Information about coping or life related to the topic.

    See https://schema.org/LivingWithHealthAspect.

    """
    type_: str = Field("LivingWithHealthAspect", const=True, alias='@type')
    

LivingWithHealthAspect.update_forward_refs()
