from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class HowItWorksHealthAspect(HealthAspectEnumeration):
    """Content that discusses and explains how a particular health-related topic works, e.g."
     "in terms of mechanisms and underlying science.

    See: https://schema.org/HowItWorksHealthAspect
    Model depth: 5
    """
    type_: str = Field("HowItWorksHealthAspect", alias='@type')
    

