from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class CommentPermission(DigitalDocumentPermissionType):
    """Permission to add comments to the document.

    See: https://schema.org/CommentPermission
    Model depth: 5
    """
    type_: str = Field("CommentPermission", alias='@type')
    

