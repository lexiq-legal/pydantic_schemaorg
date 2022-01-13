from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop.

    See: https://schema.org/AutoBodyShop
    Model depth: 5
    """

    type_: str = Field("AutoBodyShop", const=True, alias="@type")


if TYPE_CHECKING:

    AutoBodyShop.update_forward_refs()
