from pydantic import Field
from pydantic_schema_org.TypeAndQuantityNode import TypeAndQuantityNode
from typing import Any, Optional, Union, List
from pydantic_schema_org.Collection import Collection
from pydantic_schema_org.Product import Product


class ProductCollection(Collection, Product):
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
