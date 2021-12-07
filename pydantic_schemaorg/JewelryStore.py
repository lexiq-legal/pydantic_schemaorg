from pydantic import Field
from pydantic_schemaorg.Store import Store


class JewelryStore(Store):
    """A jewelry store.

    See https://schema.org/JewelryStore.

    """
    type_: str = Field("JewelryStore", const=True, alias='@type')
    

JewelryStore.update_forward_refs()
