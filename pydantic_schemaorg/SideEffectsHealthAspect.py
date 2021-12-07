from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SideEffectsHealthAspect(HealthAspectEnumeration):
    """Side effects that can be observed from the usage of the topic.

    See https://schema.org/SideEffectsHealthAspect.

    """
    type_: str = Field("SideEffectsHealthAspect", const=True, alias='@type')
    

SideEffectsHealthAspect.update_forward_refs()
