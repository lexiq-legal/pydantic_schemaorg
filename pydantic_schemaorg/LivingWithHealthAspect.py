from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class LivingWithHealthAspect(HealthAspectEnumeration):
    """Information about coping or life related to the topic.

    See https://schema.org/LivingWithHealthAspect.

    """

    locals().update({"@type": Field("LivingWithHealthAspect", const=True)})


LivingWithHealthAspect.update_forward_refs()
