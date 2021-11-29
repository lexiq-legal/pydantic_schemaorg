from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Product import Product


class IndividualProduct(Product):
    """A single, identifiable product instance (e.g. a laptop with a particular serial number).

    See https://schema.org/IndividualProduct.

    """

    serialNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The serial number or any alphanumeric identifier of a particular product. When attached"
     "to an offer, it is a shortcut for the serial number of the product included in the offer.",
    )
    locals().update({"@type": Field("IndividualProduct", const=True)})


IndividualProduct.update_forward_refs()
