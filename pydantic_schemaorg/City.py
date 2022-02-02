from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class City(AdministrativeArea):
    """A city or town.

    See: https://schema.org/City
    Model depth: 4
    """
    type_: str = Field("City", alias='@type')
    

