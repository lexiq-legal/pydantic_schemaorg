from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class ResearchOrganization(Organization):
    """A Research Organization (e.g. scientific institute, research company).

    See: https://schema.org/ResearchOrganization
    Model depth: 3
    """
    type_: str = Field("ResearchOrganization", alias='@type')
    

