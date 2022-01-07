from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import List, Optional, Union
from pydantic_schemaorg.Product import Product


class SomeProducts(Product):
    """A placeholder for multiple similar products of the same kind.

    See https://schema.org/SomeProducts.

    """
    type_: str = Field("SomeProducts", const=True, alias='@type')
    inventoryLevel: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The current approximate inventory level for the item or items.",
    )
    

SomeProducts.update_forward_refs()
