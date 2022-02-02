from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AnimalShelter(LocalBusiness):
    """Animal shelter.

    See: https://schema.org/AnimalShelter
    Model depth: 4
    """
    type_: str = Field("AnimalShelter", alias='@type')
    

