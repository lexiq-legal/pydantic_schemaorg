from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class State(AdministrativeArea):
    """A state or province of a country.

    See: https://schema.org/State
    Model depth: 4
    """
    type_: str = Field("State", alias='@type')
    

