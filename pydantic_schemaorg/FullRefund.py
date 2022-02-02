from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class FullRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done in the full amount the customer paid for the product

    See: https://schema.org/FullRefund
    Model depth: 5
    """
    type_: str = Field("FullRefund", alias='@type')
    

