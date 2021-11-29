from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HalalDiet(RestrictedDiet):
    """A diet conforming to Islamic dietary practices.

    See https://schema.org/HalalDiet.

    """

    locals().update({"@type": Field("HalalDiet", const=True)})


HalalDiet.update_forward_refs()
