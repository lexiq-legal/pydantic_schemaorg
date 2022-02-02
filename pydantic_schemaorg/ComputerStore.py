from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class ComputerStore(Store):
    """A computer store.

    See: https://schema.org/ComputerStore
    Model depth: 5
    """
    type_: str = Field("ComputerStore", alias='@type')
    

