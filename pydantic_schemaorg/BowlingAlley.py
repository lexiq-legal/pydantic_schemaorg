from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """A bowling alley.

    See: https://schema.org/BowlingAlley
    Model depth: 5
    """

    type_: str = Field("BowlingAlley", const=True, alias="@type")


if TYPE_CHECKING:

    BowlingAlley.update_forward_refs()
