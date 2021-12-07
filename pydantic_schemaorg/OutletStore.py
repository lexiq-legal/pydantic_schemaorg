from pydantic import Field
from pydantic_schemaorg.Store import Store


class OutletStore(Store):
    """An outlet store.

    See https://schema.org/OutletStore.

    """
    type_: str = Field("OutletStore", const=True, alias='@type')
    

OutletStore.update_forward_refs()
