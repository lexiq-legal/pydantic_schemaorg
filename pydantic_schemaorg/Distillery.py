from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """A distillery.

    See https://schema.org/Distillery.

    """

    locals().update({"@type": Field("Distillery", const=True)})


Distillery.update_forward_refs()
