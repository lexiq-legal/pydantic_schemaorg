from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class PaymentStatusType(StatusEnumeration):
    """A specific payment status. For example, PaymentDue, PaymentComplete, etc.

    See https://schema.org/PaymentStatusType.

    """

    locals().update({"@type": Field("PaymentStatusType", const=True)})


PaymentStatusType.update_forward_refs()
