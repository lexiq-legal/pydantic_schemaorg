from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class DiabeticDiet(RestrictedDiet):
    """A diet appropriate for people with diabetes.

    See https://schema.org/DiabeticDiet.

    """

    locals().update({"@type": Field("DiabeticDiet", const=True)})


DiabeticDiet.update_forward_refs()
