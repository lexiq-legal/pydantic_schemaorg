from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class PaymentDeclined(PaymentStatusType):
    """The payee received the payment, but it was declined for some reason.

    See: https://schema.org/PaymentDeclined
    Model depth: 6
    """

    type_: str = Field("PaymentDeclined", const=True, alias="@type")


if TYPE_CHECKING:

    PaymentDeclined.update_forward_refs()
