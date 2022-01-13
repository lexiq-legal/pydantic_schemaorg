from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.CreativeWork import CreativeWork


class WebPageElement(CreativeWork):
    """A web page element, like a table or an image.

    See: https://schema.org/WebPageElement
    Model depth: 3
    """

    type_: str = Field("WebPageElement", const=True, alias="@type")
    xpath: "Optional[Union[List[str], str]]" = Field(
        None,
        description="An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter"
        'case, multiple matches within a page can constitute a single conceptual "Web page element".',
    )
    cssSelector: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the"
        'latter case, multiple matches within a page can constitute a single conceptual "Web'
        'page element".',
    )


if TYPE_CHECKING:

    WebPageElement.update_forward_refs()
