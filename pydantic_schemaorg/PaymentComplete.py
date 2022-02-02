from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentComplete(PaymentStatusType):
    """The payment has been received and processed.

    See: https://schema.org/PaymentComplete
    Model depth: 6
    """
    type_: str = Field("PaymentComplete", alias='@type')
    

