from pydantic import Field
from pydantic_schemaorg.Store import Store


class PetStore(Store):
    """A pet store.

    See https://schema.org/PetStore.

    """
    type_: str = Field("PetStore", const=True, alias='@type')
    

PetStore.update_forward_refs()
