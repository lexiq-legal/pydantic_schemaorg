from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HinduDiet(RestrictedDiet):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    See https://schema.org/HinduDiet.

    """
    type_: str = Field("HinduDiet", const=True, alias='@type')
    

HinduDiet.update_forward_refs()
