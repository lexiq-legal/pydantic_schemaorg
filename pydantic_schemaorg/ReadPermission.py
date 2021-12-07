from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class ReadPermission(DigitalDocumentPermissionType):
    """Permission to read or view the document.

    See https://schema.org/ReadPermission.

    """
    type_: str = Field("ReadPermission", const=True, alias='@type')
    

ReadPermission.update_forward_refs()
