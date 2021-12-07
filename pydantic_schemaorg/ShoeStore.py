from pydantic import Field
from pydantic_schemaorg.Store import Store


class ShoeStore(Store):
    """A shoe store.

    See https://schema.org/ShoeStore.

    """
    type_: str = Field("ShoeStore", const=True, alias='@type')
    

ShoeStore.update_forward_refs()
