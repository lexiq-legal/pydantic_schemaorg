from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentAutomaticallyApplied(PaymentStatusType):
    """An automatic payment system is in place and will be used.

    See: https://schema.org/PaymentAutomaticallyApplied
    Model depth: 6
    """

    type_: str = Field("PaymentAutomaticallyApplied", const=True, alias="@type")


if TYPE_CHECKING:

    PaymentAutomaticallyApplied.update_forward_refs()
