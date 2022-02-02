from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Article import Article


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting,"
     "specifications, etc.

    See: https://schema.org/TechArticle
    Model depth: 4
    """
    type_: str = Field("TechArticle", alias='@type')
    proficiencyLevel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Proficiency needed for this content; expected values: 'Beginner', 'Expert'.",
    )
    dependencies: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Prerequisites needed to fulfill steps in article.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
