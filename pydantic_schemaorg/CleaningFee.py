from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class CleaningFee(PriceComponentTypeEnumeration):
    """Represents the cleaning fee part of the total price for an offered product, for example"
     "a vacation rental.

    See https://schema.org/CleaningFee.

    """
    type_: str = Field("CleaningFee", const=True, alias='@type')
    

CleaningFee.update_forward_refs()
