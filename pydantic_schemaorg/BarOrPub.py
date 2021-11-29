from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """A bar or pub.

    See https://schema.org/BarOrPub.

    """

    locals().update({"@type": Field("BarOrPub", const=True)})


BarOrPub.update_forward_refs()
