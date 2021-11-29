from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VegetarianDiet(RestrictedDiet):
    """A diet exclusive of animal meat.

    See https://schema.org/VegetarianDiet.

    """

    locals().update({"@type": Field("VegetarianDiet", const=True)})


VegetarianDiet.update_forward_refs()
