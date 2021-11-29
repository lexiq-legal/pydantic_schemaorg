from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowFatDiet(RestrictedDiet):
    """A diet focused on reduced fat and cholesterol intake.

    See https://schema.org/LowFatDiet.

    """

    locals().update({"@type": Field("LowFatDiet", const=True)})


LowFatDiet.update_forward_refs()
