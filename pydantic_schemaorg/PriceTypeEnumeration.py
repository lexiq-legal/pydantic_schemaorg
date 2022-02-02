from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PriceTypeEnumeration(Enumeration):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    See: https://schema.org/PriceTypeEnumeration
    Model depth: 4
    """
    type_: str = Field("PriceTypeEnumeration", alias='@type')
    

