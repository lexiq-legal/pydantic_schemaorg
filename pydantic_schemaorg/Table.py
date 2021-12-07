from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class Table(WebPageElement):
    """A table on a Web page.

    See https://schema.org/Table.

    """
    type_: str = Field("Table", const=True, alias='@type')
    

Table.update_forward_refs()
