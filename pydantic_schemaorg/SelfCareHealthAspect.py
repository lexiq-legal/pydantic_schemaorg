from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SelfCareHealthAspect(HealthAspectEnumeration):
    """Self care actions or measures that can be taken to sooth, health or avoid a topic. This"
     "may be carried at home and can be carried/managed by the person itself.

    See: https://schema.org/SelfCareHealthAspect
    Model depth: 5
    """
    type_: str = Field("SelfCareHealthAspect", alias='@type')
    

