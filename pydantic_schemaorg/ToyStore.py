from pydantic import Field
from pydantic_schemaorg.Store import Store


class ToyStore(Store):
    """A toy store.

    See https://schema.org/ToyStore.

    """
    type_: str = Field("ToyStore", const=True, alias='@type')
    

ToyStore.update_forward_refs()
