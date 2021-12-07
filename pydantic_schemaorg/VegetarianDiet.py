from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VegetarianDiet(RestrictedDiet):
    """A diet exclusive of animal meat.

    See https://schema.org/VegetarianDiet.

    """
    type_: str = Field("VegetarianDiet", const=True, alias='@type')
    

VegetarianDiet.update_forward_refs()
