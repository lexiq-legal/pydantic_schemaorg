from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PriceComponentTypeEnumeration(Enumeration):
    """Enumerates different price components that together make up the total price for an offered"
     "product.

    See https://schema.org/PriceComponentTypeEnumeration.

    """
    type_: str = Field("PriceComponentTypeEnumeration", const=True, alias='@type')
    

PriceComponentTypeEnumeration.update_forward_refs()
