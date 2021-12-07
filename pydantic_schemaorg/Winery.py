from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Winery(FoodEstablishment):
    """A winery.

    See https://schema.org/Winery.

    """
    type_: str = Field("Winery", const=True, alias='@type')
    

Winery.update_forward_refs()
