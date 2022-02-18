from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebSite(CreativeWork):
    """A WebSite is a set of related web pages and other items typically served from a single web"
     "domain and accessible via URLs.

    See: https://schema.org/WebSite
    Model depth: 3
    """
    type_: str = Field(default="WebSite", alias='@type', const=True)
    issn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
