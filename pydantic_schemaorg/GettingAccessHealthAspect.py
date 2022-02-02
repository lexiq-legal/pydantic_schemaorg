from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class GettingAccessHealthAspect(HealthAspectEnumeration):
    """Content that discusses practical and policy aspects for getting access to specific"
     "kinds of healthcare (e.g. distribution mechanisms for vaccines).

    See: https://schema.org/GettingAccessHealthAspect
    Model depth: 5
    """
    type_: str = Field("GettingAccessHealthAspect", alias='@type')
    

