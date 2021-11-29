from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """A type of permission which can be granted for accessing a digital document.

    See https://schema.org/DigitalDocumentPermissionType.

    """

    locals().update({"@type": Field("DigitalDocumentPermissionType", const=True)})


DigitalDocumentPermissionType.update_forward_refs()
