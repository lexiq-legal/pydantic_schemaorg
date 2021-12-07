from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class FullRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done in the full amount the customer paid for the product

    See https://schema.org/FullRefund.

    """
    type_: str = Field("FullRefund", const=True, alias='@type')
    

FullRefund.update_forward_refs()
