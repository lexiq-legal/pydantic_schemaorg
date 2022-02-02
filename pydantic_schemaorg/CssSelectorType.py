from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Text import Text


class CssSelectorType(Text):
    """Text representing a CSS selector.

    See: https://schema.org/CssSelectorType
    Model depth: 6
    """
    type_: str = Field("CssSelectorType", alias='@type')
    

