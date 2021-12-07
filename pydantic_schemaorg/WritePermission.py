from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class WritePermission(DigitalDocumentPermissionType):
    """Permission to write or edit the document.

    See https://schema.org/WritePermission.

    """
    type_: str = Field("WritePermission", const=True, alias='@type')
    

WritePermission.update_forward_refs()
