from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowLactoseDiet(RestrictedDiet):
    """A diet appropriate for people with lactose intolerance.

    See https://schema.org/LowLactoseDiet.

    """
    type_: str = Field("LowLactoseDiet", const=True, alias='@type')
    

LowLactoseDiet.update_forward_refs()
