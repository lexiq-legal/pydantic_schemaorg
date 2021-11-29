from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HinduDiet(RestrictedDiet):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    See https://schema.org/HinduDiet.

    """

    locals().update({"@type": Field("HinduDiet", const=True)})


HinduDiet.update_forward_refs()
