from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class ExchangeRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done as an exchange for the same product.

    See https://schema.org/ExchangeRefund.

    """
    type_: str = Field("ExchangeRefund", const=True, alias='@type')
    

ExchangeRefund.update_forward_refs()
