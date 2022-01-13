from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool.

    See: https://schema.org/PublicSwimmingPool
    Model depth: 5
    """

    type_: str = Field("PublicSwimmingPool", const=True, alias="@type")


if TYPE_CHECKING:

    PublicSwimmingPool.update_forward_refs()
