from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """A distillery.

    See https://schema.org/Distillery.

    """
    type_: str = Field("Distillery", const=True, alias='@type')
    

Distillery.update_forward_refs()
