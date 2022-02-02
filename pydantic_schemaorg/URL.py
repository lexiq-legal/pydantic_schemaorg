from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Text import Text


class URL(Text):
    """Data type: URL.

    See: https://schema.org/URL
    Model depth: 6
    """
    type_: str = Field("URL", alias='@type')
    

