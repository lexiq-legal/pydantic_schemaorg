from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType


class WritePermission(DigitalDocumentPermissionType):
    """Permission to write or edit the document.

    See: https://schema.org/WritePermission
    Model depth: 5
    """
    type_: str = Field("WritePermission", alias='@type')
    

