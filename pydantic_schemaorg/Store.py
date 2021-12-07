from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Store(LocalBusiness):
    """A retail good store.

    See https://schema.org/Store.

    """
    type_: str = Field("Store", const=True, alias='@type')
    

Store.update_forward_refs()
