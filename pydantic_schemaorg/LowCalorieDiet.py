from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowCalorieDiet(RestrictedDiet):
    """A diet focused on reduced calorie intake.

    See https://schema.org/LowCalorieDiet.

    """
    type_: str = Field("LowCalorieDiet", const=True, alias='@type')
    

LowCalorieDiet.update_forward_refs()
