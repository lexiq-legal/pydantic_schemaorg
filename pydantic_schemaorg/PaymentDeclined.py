from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentDeclined(PaymentStatusType):
    """The payee received the payment, but it was declined for some reason.

    See https://schema.org/PaymentDeclined.

    """
    type_: str = Field("PaymentDeclined", const=True, alias='@type')
    

PaymentDeclined.update_forward_refs()
