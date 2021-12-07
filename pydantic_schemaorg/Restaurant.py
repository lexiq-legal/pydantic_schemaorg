from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """A restaurant.

    See https://schema.org/Restaurant.

    """
    type_: str = Field("Restaurant", const=True, alias='@type')
    

Restaurant.update_forward_refs()
