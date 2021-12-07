from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VeganDiet(RestrictedDiet):
    """A diet exclusive of all animal products.

    See https://schema.org/VeganDiet.

    """
    type_: str = Field("VeganDiet", const=True, alias='@type')
    

VeganDiet.update_forward_refs()
