from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


class OnSitePickup(DeliveryMethod):
    """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.

    See: https://schema.org/OnSitePickup
    Model depth: 5
    """

    type_: str = Field("OnSitePickup", const=True, alias="@type")


if TYPE_CHECKING:

    OnSitePickup.update_forward_refs()
