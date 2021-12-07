from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class CausesHealthAspect(HealthAspectEnumeration):
    """Information about the causes and main actions that gave rise to the topic.

    See https://schema.org/CausesHealthAspect.

    """
    type_: str = Field("CausesHealthAspect", const=True, alias='@type')
    

CausesHealthAspect.update_forward_refs()
