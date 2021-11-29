from pydantic import Field
from pydantic_schema_org.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class ReadPermission(DigitalDocumentPermissionType):
    """Permission to read or view the document.

    See https://schema.org/ReadPermission.

    """

    locals().update({"@type": Field("ReadPermission", const=True)})


ReadPermission.update_forward_refs()
