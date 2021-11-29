from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebSite(CreativeWork):
    """A WebSite is a set of related web pages and other items typically served from a single web"
     "domain and accessible via URLs.

    See https://schema.org/WebSite.

    """

    issn: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    locals().update({"@type": Field("WebSite", const=True)})


WebSite.update_forward_refs()
