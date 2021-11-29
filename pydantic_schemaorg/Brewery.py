from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """Brewery.

    See https://schema.org/Brewery.

    """

    locals().update({"@type": Field("Brewery", const=True)})


Brewery.update_forward_refs()
