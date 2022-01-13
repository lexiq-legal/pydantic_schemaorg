from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """A car rental business.

    See: https://schema.org/AutoRental
    Model depth: 5
    """

    type_: str = Field("AutoRental", const=True, alias="@type")


if TYPE_CHECKING:

    AutoRental.update_forward_refs()
