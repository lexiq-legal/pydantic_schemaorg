from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PriceTypeEnumeration(Enumeration):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    See https://schema.org/PriceTypeEnumeration.

    """
    type_: str = Field("PriceTypeEnumeration", const=True, alias='@type')
    

PriceTypeEnumeration.update_forward_refs()
