from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """A specific payment status. For example, PaymentDue, PaymentComplete, etc.

    See: https://schema.org/PaymentStatusType
    Model depth: 5
    """
    type_: str = Field("PaymentStatusType", alias='@type')
    

