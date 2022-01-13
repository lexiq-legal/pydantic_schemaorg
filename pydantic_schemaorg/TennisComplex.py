from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class TennisComplex(SportsActivityLocation):
    """A tennis complex.

    See: https://schema.org/TennisComplex
    Model depth: 5
    """

    type_: str = Field("TennisComplex", const=True, alias="@type")


if TYPE_CHECKING:

    TennisComplex.update_forward_refs()
