from pydantic import Field
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Product import Product


class ProductGroup(Product):
    """A ProductGroup represents a group of [[Product]]s that vary only in certain well-described"
     "ways, such as by [[size]], [[color]], [[material]] etc. While a ProductGroup itself"
     "is not directly offered for sale, the various varying products that it represents can"
     "be. The ProductGroup serves as a prototype or template, standing in for all of the products"
     "who have an [[isVariantOf]] relationship to it. As such, properties (including additional"
     "types) can be applied to the ProductGroup to represent characteristics shared by each"
     "of the (possibly very many) variants. Properties that reference a ProductGroup are"
     "not included in this mechanism; neither are the following specific properties [[variesBy]],"
     "[[hasVariant]], [[url]].

    See https://schema.org/ProductGroup.

    """

    variesBy: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="Indicates the property or properties by which the variants in a [[ProductGroup]] vary,"
     "e.g. their size, color etc. Schema.org properties can be referenced by their short name"
     "e.g. \"color\"; terms defined elsewhere can be referenced with their URIs.",
    )
    productGroupID: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates a textual identifier for a ProductGroup.",
    )
    hasVariant: Optional[Union[List[Product], Product]] = Field(
        None,
        description="Indicates a [[Product]] that is a member of this [[ProductGroup]] (or [[ProductModel]]).",
    )
    locals().update({"@type": Field("ProductGroup", const=True)})


ProductGroup.update_forward_refs()
