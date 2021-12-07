from pydantic import Field
from pydantic_schemaorg.Store import Store


class WholesaleStore(Store):
    """A wholesale store.

    See https://schema.org/WholesaleStore.

    """
    type_: str = Field("WholesaleStore", const=True, alias='@type')
    

WholesaleStore.update_forward_refs()
