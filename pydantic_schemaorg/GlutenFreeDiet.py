from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class GlutenFreeDiet(RestrictedDiet):
    """A diet exclusive of gluten.

    See https://schema.org/GlutenFreeDiet.

    """

    locals().update({"@type": Field("GlutenFreeDiet", const=True)})


GlutenFreeDiet.update_forward_refs()
