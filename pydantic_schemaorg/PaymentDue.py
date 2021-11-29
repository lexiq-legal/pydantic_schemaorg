from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentDue(PaymentStatusType):
    """The payment is due, but still within an acceptable time to be received.

    See https://schema.org/PaymentDue.

    """

    locals().update({"@type": Field("PaymentDue", const=True)})


PaymentDue.update_forward_refs()
