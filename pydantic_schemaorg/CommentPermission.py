from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class CommentPermission(DigitalDocumentPermissionType):
    """Permission to add comments to the document.

    See https://schema.org/CommentPermission.

    """
    type_: str = Field("CommentPermission", const=True, alias='@type')
    

CommentPermission.update_forward_refs()
