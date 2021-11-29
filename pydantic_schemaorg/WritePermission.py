from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class WritePermission(DigitalDocumentPermissionType):
    """Permission to write or edit the document.

    See https://schema.org/WritePermission.

    """

    locals().update({"@type": Field("WritePermission", const=True)})


WritePermission.update_forward_refs()
