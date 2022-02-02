from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Continent(Landform):
    """One of the continents (for example, Europe or Africa).

    See: https://schema.org/Continent
    Model depth: 4
    """
    type_: str = Field("Continent", alias='@type')
    

