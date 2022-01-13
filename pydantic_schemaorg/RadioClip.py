from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Clip import Clip


class RadioClip(Clip):
    """A short radio program or a segment/part of a radio program.

    See: https://schema.org/RadioClip
    Model depth: 4
    """

    type_: str = Field("RadioClip", const=True, alias="@type")


if TYPE_CHECKING:

    RadioClip.update_forward_refs()
