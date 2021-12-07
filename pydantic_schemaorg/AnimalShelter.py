from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AnimalShelter(LocalBusiness):
    """Animal shelter.

    See https://schema.org/AnimalShelter.

    """
    type_: str = Field("AnimalShelter", const=True, alias='@type')
    

AnimalShelter.update_forward_refs()
