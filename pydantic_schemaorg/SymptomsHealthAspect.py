from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SymptomsHealthAspect(HealthAspectEnumeration):
    """Symptoms or related symptoms of a Topic.

    See https://schema.org/SymptomsHealthAspect.

    """
    type_: str = Field("SymptomsHealthAspect", const=True, alias='@type')
    

SymptomsHealthAspect.update_forward_refs()
