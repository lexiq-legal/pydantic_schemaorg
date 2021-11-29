from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SymptomsHealthAspect(HealthAspectEnumeration):
    """Symptoms or related symptoms of a Topic.

    See https://schema.org/SymptomsHealthAspect.

    """

    locals().update({"@type": Field("SymptomsHealthAspect", const=True)})


SymptomsHealthAspect.update_forward_refs()
