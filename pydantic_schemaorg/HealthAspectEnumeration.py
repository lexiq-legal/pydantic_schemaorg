from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class HealthAspectEnumeration(Enumeration):
    """HealthAspectEnumeration enumerates several aspects of health content online, each"
     "of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    See: https://schema.org/HealthAspectEnumeration
    Model depth: 4
    """
    type_: str = Field("HealthAspectEnumeration", alias='@type')
    

