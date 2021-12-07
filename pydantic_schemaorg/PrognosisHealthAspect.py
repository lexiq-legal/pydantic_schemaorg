from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PrognosisHealthAspect(HealthAspectEnumeration):
    """Typical progression and happenings of life course of the topic.

    See https://schema.org/PrognosisHealthAspect.

    """
    type_: str = Field("PrognosisHealthAspect", const=True, alias='@type')
    

PrognosisHealthAspect.update_forward_refs()
