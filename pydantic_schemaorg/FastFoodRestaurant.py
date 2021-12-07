from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant.

    See https://schema.org/FastFoodRestaurant.

    """
    type_: str = Field("FastFoodRestaurant", const=True, alias='@type')
    

FastFoodRestaurant.update_forward_refs()
