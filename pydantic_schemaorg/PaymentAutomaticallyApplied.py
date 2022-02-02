from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentAutomaticallyApplied(PaymentStatusType):
    """An automatic payment system is in place and will be used.

    See: https://schema.org/PaymentAutomaticallyApplied
    Model depth: 6
    """
    type_: str = Field("PaymentAutomaticallyApplied", alias='@type')
    

