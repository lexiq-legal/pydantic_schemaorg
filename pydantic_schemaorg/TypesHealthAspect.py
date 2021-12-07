from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TypesHealthAspect(HealthAspectEnumeration):
    """Categorization and other types related to a topic.

    See https://schema.org/TypesHealthAspect.

    """
    type_: str = Field("TypesHealthAspect", const=True, alias='@type')
    

TypesHealthAspect.update_forward_refs()
