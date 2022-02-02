from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class Table(WebPageElement):
    """A table on a Web page.

    See: https://schema.org/Table
    Model depth: 4
    """
    type_: str = Field("Table", alias='@type')
    

