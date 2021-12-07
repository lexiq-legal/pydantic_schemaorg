from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentPastDue(PaymentStatusType):
    """The payment is due and considered late.

    See https://schema.org/PaymentPastDue.

    """
    type_: str = Field("PaymentPastDue", const=True, alias='@type')
    

PaymentPastDue.update_forward_refs()
