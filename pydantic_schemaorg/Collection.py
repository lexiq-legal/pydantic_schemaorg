from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class Collection(CreativeWork):
    """A collection of items e.g. creative works or products.

    See https://schema.org/Collection.

    """
    type_: str = Field("Collection", const=True, alias='@type')
    collectionSize: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of items in the [[Collection]].",
    )
    

Collection.update_forward_refs()
