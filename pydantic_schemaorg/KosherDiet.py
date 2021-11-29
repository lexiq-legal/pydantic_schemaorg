from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class KosherDiet(RestrictedDiet):
    """A diet conforming to Jewish dietary practices.

    See https://schema.org/KosherDiet.

    """

    locals().update({"@type": Field("KosherDiet", const=True)})


KosherDiet.update_forward_refs()
