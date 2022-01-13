from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


class LockerDelivery(DeliveryMethod):
    """A DeliveryMethod in which an item is made available via locker.

    See: https://schema.org/LockerDelivery
    Model depth: 5
    """

    type_: str = Field("LockerDelivery", const=True, alias="@type")


if TYPE_CHECKING:

    LockerDelivery.update_forward_refs()
