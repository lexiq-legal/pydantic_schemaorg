from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class CausesHealthAspect(HealthAspectEnumeration):
    """Information about the causes and main actions that gave rise to the topic.

    See https://schema.org/CausesHealthAspect.

    """

    locals().update({"@type": Field("CausesHealthAspect", const=True)})


CausesHealthAspect.update_forward_refs()
