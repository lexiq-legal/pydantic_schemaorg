from pydantic import Field
from pydantic_schemaorg.Store import Store


class SportingGoodsStore(Store):
    """A sporting goods store.

    See https://schema.org/SportingGoodsStore.

    """
    type_: str = Field("SportingGoodsStore", const=True, alias='@type')
    

SportingGoodsStore.update_forward_refs()
