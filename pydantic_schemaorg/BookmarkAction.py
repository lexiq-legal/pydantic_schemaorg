from pydantic import Field
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class BookmarkAction(OrganizeAction):
    """An agent bookmarks/flags/labels/tags/marks an object.

    See https://schema.org/BookmarkAction.

    """

    locals().update({"@type": Field("BookmarkAction", const=True)})


BookmarkAction.update_forward_refs()
