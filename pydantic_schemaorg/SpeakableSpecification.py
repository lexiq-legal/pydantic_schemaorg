from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class SpeakableSpecification(Intangible):
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]])"
     "sections of a document that are highlighted as particularly [[speakable]]. Instances"
     "of this type are expected to be used primarily as values of the [[speakable]] property.

    See: https://schema.org/SpeakableSpecification
    Model depth: 3
    """

    type_: str = Field("SpeakableSpecification", const=True, alias="@type")
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

    SpeakableSpecification.update_forward_refs()
