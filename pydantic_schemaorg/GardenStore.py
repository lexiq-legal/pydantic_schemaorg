from pydantic import Field
from pydantic_schemaorg.Store import Store


class GardenStore(Store):
    """A garden store.

    See https://schema.org/GardenStore.

    """
    type_: str = Field("GardenStore", const=True, alias='@type')
    

GardenStore.update_forward_refs()
