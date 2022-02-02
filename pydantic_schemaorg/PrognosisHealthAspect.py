from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PrognosisHealthAspect(HealthAspectEnumeration):
    """Typical progression and happenings of life course of the topic.

    See: https://schema.org/PrognosisHealthAspect
    Model depth: 5
    """
    type_: str = Field("PrognosisHealthAspect", alias='@type')
    

