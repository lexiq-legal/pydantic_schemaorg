from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class AlignmentObject(Intangible):
    """An intangible item that describes an alignment between a learning resource and a node"
     "in an educational framework. Should not be used where the nature of the alignment can"
     "be described using a simple property, for example to express that a resource [[teaches]]"
     "or [[assesses]] a competency.

    See: https://schema.org/AlignmentObject
    Model depth: 3
    """
    type_: str = Field("AlignmentObject", alias='@type')
    alignmentType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A category of alignment between the learning resource and the framework node. Recommended"
     "values include: 'requires', 'textComplexity', 'readingLevel', and 'educationalSubject'.",
    )
    targetUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="The URL of a node in an established educational framework.",
    )
    targetDescription: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The description of a node in an established educational framework.",
    )
    educationalFramework: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The framework to which the resource being described is aligned.",
    )
    targetName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The name of a node in an established educational framework.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
