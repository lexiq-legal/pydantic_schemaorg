from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Painting(CreativeWork):
    """A painting.

    See: https://schema.org/Painting
    Model depth: 3
    """

    type_: str = Field("Painting", const=True, alias="@type")


if TYPE_CHECKING:

    Painting.update_forward_refs()
