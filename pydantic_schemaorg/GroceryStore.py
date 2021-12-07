from pydantic import Field
from pydantic_schemaorg.Store import Store


class GroceryStore(Store):
    """A grocery store.

    See https://schema.org/GroceryStore.

    """
    type_: str = Field("GroceryStore", const=True, alias='@type')
    

GroceryStore.update_forward_refs()
