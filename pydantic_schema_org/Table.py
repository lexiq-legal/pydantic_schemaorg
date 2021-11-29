from pydantic import Field
from pydantic_schema_org.WebPageElement import WebPageElement


class Table(WebPageElement):
    """A table on a Web page.

    See https://schema.org/Table.

    """

    locals().update({"@type": Field("Table", const=True)})


Table.update_forward_refs()
