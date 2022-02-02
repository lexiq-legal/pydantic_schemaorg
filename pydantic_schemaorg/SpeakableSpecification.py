from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class SpeakableSpecification(Intangible):
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]])"
     "sections of a document that are highlighted as particularly [[speakable]]. Instances"
     "of this type are expected to be used primarily as values of the [[speakable]] property.

    See: https://schema.org/SpeakableSpecification
    Model depth: 3
    """
    type_: str = Field("SpeakableSpecification", alias='@type')
    xpath: Optional[Union[List[Union[str, 'XPathType']], str, 'XPathType']] = Field(
        None,
        description="An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter"
     "case, multiple matches within a page can constitute a single conceptual \"Web page element\".",
    )
    cssSelector: Optional[Union[List[Union[str, 'CssSelectorType']], str, 'CssSelectorType']] = Field(
        None,
        description="A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the"
     "latter case, multiple matches within a page can constitute a single conceptual \"Web"
     "page element\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.XPathType import XPathType
    from pydantic_schemaorg.CssSelectorType import CssSelectorType
