from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class Country(AdministrativeArea):
    """A country.

    See: https://schema.org/Country
    Model depth: 4
    """
    type_: str = Field("Country", alias='@type')
    

