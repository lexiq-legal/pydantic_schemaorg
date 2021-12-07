from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """A bakery.

    See https://schema.org/Bakery.

    """
    type_: str = Field("Bakery", const=True, alias='@type')
    

Bakery.update_forward_refs()
