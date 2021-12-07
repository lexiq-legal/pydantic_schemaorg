from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class StoreCreditRefund(RefundTypeEnumeration):
    """Specifies that the customer receives a store credit as refund when returning a product

    See https://schema.org/StoreCreditRefund.

    """
    type_: str = Field("StoreCreditRefund", const=True, alias='@type')
    

StoreCreditRefund.update_forward_refs()
