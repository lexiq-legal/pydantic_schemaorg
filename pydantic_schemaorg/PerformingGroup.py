from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class PerformingGroup(Organization):
    """A performance group, such as a band, an orchestra, or a circus.

    See: https://schema.org/PerformingGroup
    Model depth: 3
    """
    type_: str = Field("PerformingGroup", alias='@type')
    

