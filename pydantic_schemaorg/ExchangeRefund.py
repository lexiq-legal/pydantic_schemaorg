from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class ExchangeRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done as an exchange for the same product.

    See https://schema.org/ExchangeRefund.

    """

    locals().update({"@type": Field("ExchangeRefund", const=True)})


ExchangeRefund.update_forward_refs()
