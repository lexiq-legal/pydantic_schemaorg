from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Article import Article


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting,"
     "specifications, etc.

    See https://schema.org/TechArticle.

    """
    type_: str = Field("TechArticle", const=True, alias='@type')
    proficiencyLevel: Optional[Union[List[str], str]] = Field(
        None,
        description="Proficiency needed for this content; expected values: 'Beginner', 'Expert'.",
    )
    dependencies: Optional[Union[List[str], str]] = Field(
        None,
        description="Prerequisites needed to fulfill steps in article.",
    )
    

TechArticle.update_forward_refs()
