from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class PrognosisHealthAspect(HealthAspectEnumeration):
    """Typical progression and happenings of life course of the topic.

    See https://schema.org/PrognosisHealthAspect.

    """

    locals().update({"@type": Field("PrognosisHealthAspect", const=True)})


PrognosisHealthAspect.update_forward_refs()
