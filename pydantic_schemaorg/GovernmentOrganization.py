from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class GovernmentOrganization(Organization):
    """A governmental organization or agency.

    See: https://schema.org/GovernmentOrganization
    Model depth: 3
    """
    type_: str = Field("GovernmentOrganization", alias='@type')
    

