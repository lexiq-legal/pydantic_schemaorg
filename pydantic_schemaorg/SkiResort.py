from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Resort import Resort

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SkiResort(Resort, SportsActivityLocation):
    """A ski resort.

    See: https://schema.org/SkiResort
    Model depth: 5
    """

    type_: str = Field("SkiResort", const=True, alias="@type")


if TYPE_CHECKING:

    SkiResort.update_forward_refs()
