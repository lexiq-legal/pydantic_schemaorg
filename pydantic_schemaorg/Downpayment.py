from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Downpayment(PriceComponentTypeEnumeration):
    """Represents the downpayment (up-front payment) price component of the total price for"
     "an offered product that has additional installment payments.

    See https://schema.org/Downpayment.

    """

    locals().update({"@type": Field("Downpayment", const=True)})


Downpayment.update_forward_refs()
