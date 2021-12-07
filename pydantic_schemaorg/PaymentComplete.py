from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentComplete(PaymentStatusType):
    """The payment has been received and processed.

    See https://schema.org/PaymentComplete.

    """
    type_: str = Field("PaymentComplete", const=True, alias='@type')
    

PaymentComplete.update_forward_refs()
