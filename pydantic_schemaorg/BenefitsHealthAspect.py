from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class BenefitsHealthAspect(HealthAspectEnumeration):
    """Content about the benefits and advantages of usage or utilization of topic.

    See: https://schema.org/BenefitsHealthAspect
    Model depth: 5
    """
    type_: str = Field("BenefitsHealthAspect", alias='@type')
    

