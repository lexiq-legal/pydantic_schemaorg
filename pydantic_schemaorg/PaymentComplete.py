from pydantic import Field
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentComplete(PaymentStatusType):
    """The payment has been received and processed.

    See https://schema.org/PaymentComplete.

    """

    locals().update({"@type": Field("PaymentComplete", const=True)})


PaymentComplete.update_forward_refs()
