from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Intangible import Intangible


class SpeakableSpecification(Intangible):
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]])"
     "sections of a document that are highlighted as particularly [[speakable]]. Instances"
     "of this type are expected to be used primarily as values of the [[speakable]] property.

    See https://schema.org/SpeakableSpecification.

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
    locals().update({"@type": Field("SpeakableSpecification", const=True)})


SpeakableSpecification.update_forward_refs()
