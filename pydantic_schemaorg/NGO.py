from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class NGO(Organization):
    """Organization: Non-governmental Organization.

    See: https://schema.org/NGO
    Model depth: 3
    """
    type_: str = Field("NGO", alias='@type')
    

