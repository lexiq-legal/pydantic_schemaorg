from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Product import Product


class SomeProducts(Product):
    """A placeholder for multiple similar products of the same kind.

    See https://schema.org/SomeProducts.

    """
    type_: str = Field("SomeProducts", const=True, alias='@type')
    inventoryLevel: Any = Field(
        None,
        description="The current approximate inventory level for the item or items.",
    )
    

SomeProducts.update_forward_refs()
