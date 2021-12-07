from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class KosherDiet(RestrictedDiet):
    """A diet conforming to Jewish dietary practices.

    See https://schema.org/KosherDiet.

    """
    type_: str = Field("KosherDiet", const=True, alias='@type')
    

KosherDiet.update_forward_refs()
