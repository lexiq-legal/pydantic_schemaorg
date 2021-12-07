from pydantic import Field
from pydantic_schemaorg.Store import Store


class TireShop(Store):
    """A tire shop.

    See https://schema.org/TireShop.

    """
    type_: str = Field("TireShop", const=True, alias='@type')
    

TireShop.update_forward_refs()
