from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop.

    See https://schema.org/CafeOrCoffeeShop.

    """

    locals().update({"@type": Field("CafeOrCoffeeShop", const=True)})


CafeOrCoffeeShop.update_forward_refs()
