from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class PreventionHealthAspect(HealthAspectEnumeration):
    """Information about actions or measures that can be taken to avoid getting the topic or"
     "reaching a critical situation related to the topic.

    See https://schema.org/PreventionHealthAspect.

    """

    locals().update({"@type": Field("PreventionHealthAspect", const=True)})


PreventionHealthAspect.update_forward_refs()
