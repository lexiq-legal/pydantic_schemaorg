from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Installment(PriceComponentTypeEnumeration):
    """Represents the installment pricing component of the total price for an offered product.

    See https://schema.org/Installment.

    """
    type_: str = Field("Installment", const=True, alias='@type')
    

Installment.update_forward_refs()
