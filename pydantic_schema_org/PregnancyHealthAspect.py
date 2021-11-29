from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class PregnancyHealthAspect(HealthAspectEnumeration):
    """Content discussing pregnancy-related aspects of a health topic.

    See https://schema.org/PregnancyHealthAspect.

    """

    locals().update({"@type": Field("PregnancyHealthAspect", const=True)})


PregnancyHealthAspect.update_forward_refs()
