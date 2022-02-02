from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.WebContent import WebContent


class HealthTopicContent(WebContent):
    """[[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic,"
     "e.g. a condition, its symptoms or treatments. Such content may be comprised of several"
     "parts or sections and use different types of media. Multiple instances of [[WebContent]]"
     "(and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]]"
     "where there is some kind of content hierarchy, and their content described with [[about]]"
     "and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.

    See: https://schema.org/HealthTopicContent
    Model depth: 4
    """
    type_: str = Field("HealthTopicContent", alias='@type')
    hasHealthAspect: Optional[Union[List[Union['HealthAspectEnumeration', str]], 'HealthAspectEnumeration', str]] = Field(
        None,
        description="Indicates the aspect or aspects specifically addressed in some [[HealthTopicContent]]."
     "For example, that the content is an overview, or that it talks about treatment, self-care,"
     "treatments or their side-effects.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration
