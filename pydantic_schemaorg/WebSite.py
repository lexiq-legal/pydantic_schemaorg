from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebSite(CreativeWork):
    """A WebSite is a set of related web pages and other items typically served from a single web"
     "domain and accessible via URLs.

    See https://schema.org/WebSite.

    """
    type_: str = Field("WebSite", const=True, alias='@type')
    issn: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    

WebSite.update_forward_refs()
