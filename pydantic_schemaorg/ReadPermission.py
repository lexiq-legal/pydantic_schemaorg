from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class ReadPermission(DigitalDocumentPermissionType):
    """Permission to read or view the document.

    See: https://schema.org/ReadPermission
    Model depth: 5
    """
    type_: str = Field("ReadPermission", alias='@type')
    

