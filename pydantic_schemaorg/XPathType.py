from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Text import Text


class XPathType(Text):
    """Text representing an XPath (typically but not necessarily version 1.0).

    See: https://schema.org/XPathType
    Model depth: 6
    """
    type_: str = Field("XPathType", alias='@type')
    

