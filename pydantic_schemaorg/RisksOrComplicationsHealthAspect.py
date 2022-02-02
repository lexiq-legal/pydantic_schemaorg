from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RisksOrComplicationsHealthAspect(HealthAspectEnumeration):
    """Information about the risk factors and possible complications that may follow a topic.

    See: https://schema.org/RisksOrComplicationsHealthAspect
    Model depth: 5
    """
    type_: str = Field("RisksOrComplicationsHealthAspect", alias='@type')
    

