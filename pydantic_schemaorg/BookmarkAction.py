from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrganizeAction import OrganizeAction


class BookmarkAction(OrganizeAction):
    """An agent bookmarks/flags/labels/tags/marks an object.

    See: https://schema.org/BookmarkAction
    Model depth: 4
    """

    type_: str = Field("BookmarkAction", const=True, alias="@type")


if TYPE_CHECKING:

    BookmarkAction.update_forward_refs()
