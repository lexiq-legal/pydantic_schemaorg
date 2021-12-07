from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RelatedTopicsHealthAspect(HealthAspectEnumeration):
    """Other prominent or relevant topics tied to the main topic.

    See https://schema.org/RelatedTopicsHealthAspect.

    """
    type_: str = Field("RelatedTopicsHealthAspect", const=True, alias='@type')
    

RelatedTopicsHealthAspect.update_forward_refs()
