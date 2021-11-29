from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SafetyHealthAspect(HealthAspectEnumeration):
    """Content about the safety-related aspects of a health topic.

    See https://schema.org/SafetyHealthAspect.

    """

    locals().update({"@type": Field("SafetyHealthAspect", const=True)})


SafetyHealthAspect.update_forward_refs()
