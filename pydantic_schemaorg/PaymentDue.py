from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentDue(PaymentStatusType):
    """The payment is due, but still within an acceptable time to be received.

    See https://schema.org/PaymentDue.

    """
    type_: str = Field("PaymentDue", const=True, alias='@type')
    

PaymentDue.update_forward_refs()
