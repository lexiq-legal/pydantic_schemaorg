from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PregnancyHealthAspect(HealthAspectEnumeration):
    """Content discussing pregnancy-related aspects of a health topic.

    See https://schema.org/PregnancyHealthAspect.

    """
    type_: str = Field("PregnancyHealthAspect", const=True, alias='@type')
    

PregnancyHealthAspect.update_forward_refs()
