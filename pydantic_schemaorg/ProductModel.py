from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Product import Product


class ProductModel(Product):
    """A datasheet or vendor specification of a product (in the sense of a prototypical description).

    See: https://schema.org/ProductModel
    Model depth: 3
    """
    type_: str = Field("ProductModel", alias='@type')
    predecessorOf: Optional[Union[List[Union['ProductModel', str]], 'ProductModel', str]] = Field(
        None,
        description="A pointer from a previous, often discontinued variant of the product to its newer variant.",
    )
    successorOf: Optional[Union[List[Union['ProductModel', str]], 'ProductModel', str]] = Field(
        None,
        description="A pointer from a newer variant of a product to its previous, often discontinued predecessor.",
    )
    isVariantOf: Optional[Union[List[Union['ProductModel', 'ProductGroup', str]], 'ProductModel', 'ProductGroup', str]] = Field(
        None,
        description="Indicates the kind of product that this is a variant of. In the case of [[ProductModel]],"
     "this is a pointer (from a ProductModel) to a base product from which this product is a variant."
     "It is safe to infer that the variant inherits all product features from the base model,"
     "unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the"
     "group description also serves as a template, representing a set of Products that vary"
     "on explicitly defined, specific dimensions only (so it defines both a set of variants,"
     "as well as which values distinguish amongst those variants). When used with [[ProductGroup]],"
     "this property can apply to any [[Product]] included in the group.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ProductGroup import ProductGroup
