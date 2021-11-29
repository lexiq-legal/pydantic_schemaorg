from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class StagesHealthAspect(HealthAspectEnumeration):
    """Stages that can be observed from a topic.

    See https://schema.org/StagesHealthAspect.

    """

    locals().update({"@type": Field("StagesHealthAspect", const=True)})


StagesHealthAspect.update_forward_refs()
