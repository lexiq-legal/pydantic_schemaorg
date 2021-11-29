from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowLactoseDiet(RestrictedDiet):
    """A diet appropriate for people with lactose intolerance.

    See https://schema.org/LowLactoseDiet.

    """

    locals().update({"@type": Field("LowLactoseDiet", const=True)})


LowLactoseDiet.update_forward_refs()
