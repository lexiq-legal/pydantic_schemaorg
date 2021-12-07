from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class IngredientsHealthAspect(HealthAspectEnumeration):
    """Content discussing ingredients-related aspects of a health topic.

    See https://schema.org/IngredientsHealthAspect.

    """
    type_: str = Field("IngredientsHealthAspect", const=True, alias='@type')
    

IngredientsHealthAspect.update_forward_refs()
