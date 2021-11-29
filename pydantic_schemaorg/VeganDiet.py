from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VeganDiet(RestrictedDiet):
    """A diet exclusive of all animal products.

    See https://schema.org/VeganDiet.

    """

    locals().update({"@type": Field("VeganDiet", const=True)})


VeganDiet.update_forward_refs()
