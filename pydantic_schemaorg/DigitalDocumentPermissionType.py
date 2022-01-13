from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """A type of permission which can be granted for accessing a digital document.

    See: https://schema.org/DigitalDocumentPermissionType
    Model depth: 4
    """

    type_: str = Field("DigitalDocumentPermissionType", const=True, alias="@type")


if TYPE_CHECKING:

    DigitalDocumentPermissionType.update_forward_refs()
