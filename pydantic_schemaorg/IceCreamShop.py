from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """An ice cream shop.

    See https://schema.org/IceCreamShop.

    """
    type_: str = Field("IceCreamShop", const=True, alias='@type')
    

IceCreamShop.update_forward_refs()
