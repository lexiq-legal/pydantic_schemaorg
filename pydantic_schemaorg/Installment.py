from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Installment(PriceComponentTypeEnumeration):
    """Represents the installment pricing component of the total price for an offered product.

    See https://schema.org/Installment.

    """

    locals().update({"@type": Field("Installment", const=True)})


Installment.update_forward_refs()
