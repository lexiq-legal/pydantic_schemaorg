from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Winery(FoodEstablishment):
    """A winery.

    See https://schema.org/Winery.

    """

    locals().update({"@type": Field("Winery", const=True)})


Winery.update_forward_refs()
