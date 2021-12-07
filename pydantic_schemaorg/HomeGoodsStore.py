from pydantic import Field
from pydantic_schemaorg.Store import Store


class HomeGoodsStore(Store):
    """A home goods store.

    See https://schema.org/HomeGoodsStore.

    """
    type_: str = Field("HomeGoodsStore", const=True, alias='@type')
    

HomeGoodsStore.update_forward_refs()
