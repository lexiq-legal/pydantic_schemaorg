from pydantic import Field
from pydantic_schema_org.PaymentStatusType import PaymentStatusType


class PaymentAutomaticallyApplied(PaymentStatusType):
    """An automatic payment system is in place and will be used.

    See https://schema.org/PaymentAutomaticallyApplied.

    """

    locals().update({"@type": Field("PaymentAutomaticallyApplied", const=True)})


PaymentAutomaticallyApplied.update_forward_refs()
