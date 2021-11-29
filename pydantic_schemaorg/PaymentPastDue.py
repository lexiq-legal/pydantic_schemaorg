from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentPastDue(PaymentStatusType):
    """The payment is due and considered late.

    See https://schema.org/PaymentPastDue.

    """

    locals().update({"@type": Field("PaymentPastDue", const=True)})


PaymentPastDue.update_forward_refs()
