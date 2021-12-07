from pydantic import Field
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class BarOrPub(FoodEstablishment):
    """A bar or pub.

    See https://schema.org/BarOrPub.

    """
    type_: str = Field("BarOrPub", const=True, alias='@type')
    

BarOrPub.update_forward_refs()
