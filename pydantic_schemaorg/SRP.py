from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SRP(PriceTypeEnumeration):
    """Represents the suggested retail price (\"SRP\") of an offered product.

    See: https://schema.org/SRP
    Model depth: 5
    """
    type_: str = Field("SRP", alias='@type')
    

