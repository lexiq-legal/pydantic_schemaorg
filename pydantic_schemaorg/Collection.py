from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class Collection(CreativeWork):
    """A collection of items e.g. creative works or products.

    See https://schema.org/Collection.

    """

    collectionSize: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of items in the [[Collection]].",
    )
    locals().update({"@type": Field("Collection", const=True)})


Collection.update_forward_refs()
