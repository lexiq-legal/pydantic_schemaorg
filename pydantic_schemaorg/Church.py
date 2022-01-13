from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Church(PlaceOfWorship):
    """A church.

    See: https://schema.org/Church
    Model depth: 5
    """

    type_: str = Field("Church", const=True, alias="@type")


if TYPE_CHECKING:

    Church.update_forward_refs()
