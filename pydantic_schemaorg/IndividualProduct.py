from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Product import Product


class IndividualProduct(Product):
    """A single, identifiable product instance (e.g. a laptop with a particular serial number).

    See: https://schema.org/IndividualProduct
    Model depth: 3
    """
    type_: str = Field("IndividualProduct", alias='@type')
    serialNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The serial number or any alphanumeric identifier of a particular product. When attached"
     "to an offer, it is a shortcut for the serial number of the product included in the offer.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
