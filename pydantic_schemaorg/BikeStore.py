from pydantic import Field
from pydantic_schemaorg.Store import Store


class BikeStore(Store):
    """A bike store.

    See https://schema.org/BikeStore.

    """
    type_: str = Field("BikeStore", const=True, alias='@type')
    

BikeStore.update_forward_refs()
