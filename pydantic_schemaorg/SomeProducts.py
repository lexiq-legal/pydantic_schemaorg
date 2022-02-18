from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Product import Product


class SomeProducts(Product):
    """A placeholder for multiple similar products of the same kind.

    See: https://schema.org/SomeProducts
    Model depth: 3
    """
    type_: str = Field(default="SomeProducts", alias='@type', const=True)
    inventoryLevel: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The current approximate inventory level for the item or items.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
