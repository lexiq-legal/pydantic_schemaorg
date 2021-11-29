from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class EffectivenessHealthAspect(HealthAspectEnumeration):
    """Content about the effectiveness-related aspects of a health topic.

    See https://schema.org/EffectivenessHealthAspect.

    """

    locals().update({"@type": Field("EffectivenessHealthAspect", const=True)})


EffectivenessHealthAspect.update_forward_refs()
