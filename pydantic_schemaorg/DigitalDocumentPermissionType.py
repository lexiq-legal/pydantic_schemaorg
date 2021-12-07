from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """A type of permission which can be granted for accessing a digital document.

    See https://schema.org/DigitalDocumentPermissionType.

    """
    type_: str = Field("DigitalDocumentPermissionType", const=True, alias='@type')
    

DigitalDocumentPermissionType.update_forward_refs()
