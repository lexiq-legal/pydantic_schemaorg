from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DigitalDocumentPermissionType import (
    DigitalDocumentPermissionType,
)


class CommentPermission(DigitalDocumentPermissionType):
    """Permission to add comments to the document.

    See: https://schema.org/CommentPermission
    Model depth: 5
    """

    type_: str = Field("CommentPermission", const=True, alias="@type")


if TYPE_CHECKING:

    CommentPermission.update_forward_refs()
