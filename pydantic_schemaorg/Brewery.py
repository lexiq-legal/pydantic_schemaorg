from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """Brewery.

    See https://schema.org/Brewery.

    """
    type_: str = Field("Brewery", const=True, alias='@type')
    

Brewery.update_forward_refs()
