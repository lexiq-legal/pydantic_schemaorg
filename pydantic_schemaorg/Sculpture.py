from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Sculpture(CreativeWork):
    """A piece of sculpture.

    See: https://schema.org/Sculpture
    Model depth: 3
    """

    type_: str = Field("Sculpture", const=True, alias="@type")


if TYPE_CHECKING:

    Sculpture.update_forward_refs()
