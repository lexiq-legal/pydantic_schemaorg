from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowSaltDiet(RestrictedDiet):
    """A diet focused on reduced sodium intake.

    See https://schema.org/LowSaltDiet.

    """

    locals().update({"@type": Field("LowSaltDiet", const=True)})


LowSaltDiet.update_forward_refs()
