from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class StoreCreditRefund(RefundTypeEnumeration):
    """Specifies that the customer receives a store credit as refund when returning a product

    See: https://schema.org/StoreCreditRefund
    Model depth: 5
    """
    type_: str = Field("StoreCreditRefund", alias='@type')
    

