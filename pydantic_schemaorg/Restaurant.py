from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """A restaurant.

    See https://schema.org/Restaurant.

    """

    locals().update({"@type": Field("Restaurant", const=True)})


Restaurant.update_forward_refs()
