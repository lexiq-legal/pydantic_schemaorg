from pydantic import Field
from pydantic_schemaorg.Store import Store


class ComputerStore(Store):
    """A computer store.

    See https://schema.org/ComputerStore.

    """
    type_: str = Field("ComputerStore", const=True, alias='@type')
    

ComputerStore.update_forward_refs()
