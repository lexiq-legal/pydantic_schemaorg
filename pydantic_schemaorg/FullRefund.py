from pydantic import Field
from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


class FullRefund(RefundTypeEnumeration):
    """Specifies that a refund can be done in the full amount the customer paid for the product

    See https://schema.org/FullRefund.

    """

    locals().update({"@type": Field("FullRefund", const=True)})


FullRefund.update_forward_refs()
