from pydantic import Field
from pydantic_schemaorg.Store import Store


class HardwareStore(Store):
    """A hardware store.

    See https://schema.org/HardwareStore.

    """
    type_: str = Field("HardwareStore", const=True, alias='@type')
    

HardwareStore.update_forward_refs()
