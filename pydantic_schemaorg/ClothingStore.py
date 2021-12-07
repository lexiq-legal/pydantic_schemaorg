from pydantic import Field
from pydantic_schemaorg.Store import Store


class ClothingStore(Store):
    """A clothing store.

    See https://schema.org/ClothingStore.

    """
    type_: str = Field("ClothingStore", const=True, alias='@type')
    

ClothingStore.update_forward_refs()
