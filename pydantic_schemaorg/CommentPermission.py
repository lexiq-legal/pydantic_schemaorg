from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class CommentPermission(DigitalDocumentPermissionType):
    """Permission to add comments to the document.

    See https://schema.org/CommentPermission.

    """

    locals().update({"@type": Field("CommentPermission", const=True)})


CommentPermission.update_forward_refs()
