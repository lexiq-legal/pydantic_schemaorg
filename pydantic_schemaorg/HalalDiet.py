from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HalalDiet(RestrictedDiet):
    """A diet conforming to Islamic dietary practices.

    See https://schema.org/HalalDiet.

    """
    type_: str = Field("HalalDiet", const=True, alias='@type')
    

HalalDiet.update_forward_refs()
