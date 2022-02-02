from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Installment(PriceComponentTypeEnumeration):
    """Represents the installment pricing component of the total price for an offered product.

    See: https://schema.org/Installment
    Model depth: 5
    """
    type_: str = Field("Installment", alias='@type')
    

