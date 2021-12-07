from pydantic import Field
from pydantic_schemaorg.Store import Store


class ElectronicsStore(Store):
    """An electronics store.

    See https://schema.org/ElectronicsStore.

    """
    type_: str = Field("ElectronicsStore", const=True, alias='@type')
    

ElectronicsStore.update_forward_refs()
