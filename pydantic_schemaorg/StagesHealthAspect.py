from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class StagesHealthAspect(HealthAspectEnumeration):
    """Stages that can be observed from a topic.

    See https://schema.org/StagesHealthAspect.

    """
    type_: str = Field("StagesHealthAspect", const=True, alias='@type')
    

StagesHealthAspect.update_forward_refs()
