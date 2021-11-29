from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Bakery(FoodEstablishment):
    """A bakery.

    See https://schema.org/Bakery.

    """

    locals().update({"@type": Field("Bakery", const=True)})


Bakery.update_forward_refs()
