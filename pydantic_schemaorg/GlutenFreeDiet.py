from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class GlutenFreeDiet(RestrictedDiet):
    """A diet exclusive of gluten.

    See https://schema.org/GlutenFreeDiet.

    """
    type_: str = Field("GlutenFreeDiet", const=True, alias='@type')
    

GlutenFreeDiet.update_forward_refs()
