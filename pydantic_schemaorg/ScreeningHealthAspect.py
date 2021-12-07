from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ScreeningHealthAspect(HealthAspectEnumeration):
    """Content about how to screen or further filter a topic.

    See https://schema.org/ScreeningHealthAspect.

    """
    type_: str = Field("ScreeningHealthAspect", const=True, alias='@type')
    

ScreeningHealthAspect.update_forward_refs()
