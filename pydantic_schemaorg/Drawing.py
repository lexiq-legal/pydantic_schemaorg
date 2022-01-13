from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Drawing(CreativeWork):
    """A picture or diagram made with a pencil, pen, or crayon rather than paint.

    See: https://schema.org/Drawing
    Model depth: 3
    """

    type_: str = Field("Drawing", const=True, alias="@type")


if TYPE_CHECKING:

    Drawing.update_forward_refs()
