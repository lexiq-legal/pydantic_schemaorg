from pydantic import Field
from pydantic_schemaorg.Store import Store


class MensClothingStore(Store):
    """A men's clothing store.

    See https://schema.org/MensClothingStore.

    """
    type_: str = Field("MensClothingStore", const=True, alias='@type')
    

MensClothingStore.update_forward_refs()
