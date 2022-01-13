from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Text import Text


class XPathType(Text):
    """Text representing an XPath (typically but not necessarily version 1.0).

    See: https://schema.org/XPathType
    Model depth: 6
    """

    type_: str = Field("XPathType", const=True, alias="@type")


if TYPE_CHECKING:

    XPathType.update_forward_refs()
