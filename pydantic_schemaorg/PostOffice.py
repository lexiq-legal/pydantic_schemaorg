from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentOffice import GovernmentOffice


class PostOffice(GovernmentOffice):
    """A post office.

    See: https://schema.org/PostOffice
    Model depth: 5
    """
    type_: str = Field("PostOffice", alias='@type')
    

