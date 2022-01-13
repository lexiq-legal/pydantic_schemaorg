from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentPastDue(PaymentStatusType):
    """The payment is due and considered late.

    See: https://schema.org/PaymentPastDue
    Model depth: 6
    """

    type_: str = Field("PaymentPastDue", const=True, alias="@type")


if TYPE_CHECKING:

    PaymentPastDue.update_forward_refs()
