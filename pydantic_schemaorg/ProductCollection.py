from pydantic import Field
from pydantic_schemaorg.TypeAndQuantityNode import TypeAndQuantityNode
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.Collection import Collection


class ProductCollection(Product, Collection):
    """A set of products (either [[ProductGroup]]s or specific variants) that are listed together"
     "e.g. in an [[Offer]].

    See https://schema.org/ProductCollection.

    """

    includesObject: Optional[Union[List[TypeAndQuantityNode], TypeAndQuantityNode]] = Field(
        None,
        description="This links to a node or nodes indicating the exact quantity of the products included in"
     "an [[Offer]] or [[ProductCollection]].",
    )
    locals().update({"@type": Field("ProductCollection", const=True)})


ProductCollection.update_forward_refs()
