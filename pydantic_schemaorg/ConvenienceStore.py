from pydantic import Field
from pydantic_schemaorg.Store import Store


class ConvenienceStore(Store):
    """A convenience store.

    See https://schema.org/ConvenienceStore.

    """
    type_: str = Field("ConvenienceStore", const=True, alias='@type')
    

ConvenienceStore.update_forward_refs()
