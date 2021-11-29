from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class SideEffectsHealthAspect(HealthAspectEnumeration):
    """Side effects that can be observed from the usage of the topic.

    See https://schema.org/SideEffectsHealthAspect.

    """

    locals().update({"@type": Field("SideEffectsHealthAspect", const=True)})


SideEffectsHealthAspect.update_forward_refs()
