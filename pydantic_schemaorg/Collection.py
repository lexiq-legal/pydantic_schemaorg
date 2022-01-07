from pydantic import Field
from typing import List, Optional, Union
from pydantic_schemaorg.CreativeWork import CreativeWork


class Collection(CreativeWork):
    """A collection of items e.g. creative works or products.

    See https://schema.org/Collection.

    """
    type_: str = Field("Collection", const=True, alias='@type')
    collectionSize: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The number of items in the [[Collection]].",
    )
    

Collection.update_forward_refs()
