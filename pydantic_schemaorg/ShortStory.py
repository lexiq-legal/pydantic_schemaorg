from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class ShortStory(CreativeWork):
    """Short story or tale. A brief work of literature, usually written in narrative prose.

    See: https://schema.org/ShortStory
    Model depth: 3
    """

    type_: str = Field("ShortStory", const=True, alias="@type")


if TYPE_CHECKING:

    ShortStory.update_forward_refs()
