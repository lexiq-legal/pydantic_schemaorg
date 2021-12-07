from pydantic import Field
from pydantic_schemaorg.Store import Store


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    See https://schema.org/LiquorStore.

    """
    type_: str = Field("LiquorStore", const=True, alias='@type')
    

LiquorStore.update_forward_refs()
