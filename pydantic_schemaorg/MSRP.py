from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MSRP(PriceTypeEnumeration):
    """Represents the manufacturer suggested retail price (\"MSRP\") of an offered product.

    See: https://schema.org/MSRP
    Model depth: 5
    """
    type_: str = Field("MSRP", alias='@type')
    

