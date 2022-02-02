from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class ExchangeRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done as an exchange for the same product.

    See: https://schema.org/ExchangeRefund
    Model depth: 5
    """
    type_: str = Field("ExchangeRefund", alias='@type')
    

