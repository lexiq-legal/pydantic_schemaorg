from pydantic import Field
from pydantic_schemaorg.Store import Store


class FurnitureStore(Store):
    """A furniture store.

    See https://schema.org/FurnitureStore.

    """
    type_: str = Field("FurnitureStore", const=True, alias='@type')
    

FurnitureStore.update_forward_refs()
