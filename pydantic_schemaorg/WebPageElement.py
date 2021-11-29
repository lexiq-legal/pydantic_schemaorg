from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebPageElement(CreativeWork):
    """A web page element, like a table or an image.

    See https://schema.org/WebPageElement.

    """

    xpath: Optional[Union[List[str], str]] = Field(
        None,
        description="An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter"
     "case, multiple matches within a page can constitute a single conceptual \"Web page element\".",
    )
    cssSelector: Optional[Union[List[str], str]] = Field(
        None,
        description="A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the"
     "latter case, multiple matches within a page can constitute a single conceptual \"Web"
     "page element\".",
    )
    locals().update({"@type": Field("WebPageElement", const=True)})


WebPageElement.update_forward_refs()
