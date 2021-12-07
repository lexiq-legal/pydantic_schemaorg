from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class DiabeticDiet(RestrictedDiet):
    """A diet appropriate for people with diabetes.

    See https://schema.org/DiabeticDiet.

    """
    type_: str = Field("DiabeticDiet", const=True, alias='@type')
    

DiabeticDiet.update_forward_refs()
