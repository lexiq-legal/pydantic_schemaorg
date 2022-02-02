from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class CleaningFee(PriceComponentTypeEnumeration):
    """Represents the cleaning fee part of the total price for an offered product, for example"
     "a vacation rental.

    See: https://schema.org/CleaningFee
    Model depth: 5
    """
    type_: str = Field("CleaningFee", alias='@type')
    

