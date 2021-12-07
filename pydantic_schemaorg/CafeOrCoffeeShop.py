from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop.

    See https://schema.org/CafeOrCoffeeShop.

    """
    type_: str = Field("CafeOrCoffeeShop", const=True, alias='@type')
    

CafeOrCoffeeShop.update_forward_refs()
