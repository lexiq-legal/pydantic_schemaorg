from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowSaltDiet(RestrictedDiet):
    """A diet focused on reduced sodium intake.

    See https://schema.org/LowSaltDiet.

    """
    type_: str = Field("LowSaltDiet", const=True, alias='@type')
    

LowSaltDiet.update_forward_refs()
