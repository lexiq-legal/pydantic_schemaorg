from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowCalorieDiet(RestrictedDiet):
    """A diet focused on reduced calorie intake.

    See https://schema.org/LowCalorieDiet.

    """

    locals().update({"@type": Field("LowCalorieDiet", const=True)})


LowCalorieDiet.update_forward_refs()
