from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Article import Article


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting,"
     "specifications, etc.

    See https://schema.org/TechArticle.

    """

    proficiencyLevel: Optional[Union[List[str], str]] = Field(
        None,
        description="Proficiency needed for this content; expected values: 'Beginner', 'Expert'.",
    )
    dependencies: Optional[Union[List[str], str]] = Field(
        None,
        description="Prerequisites needed to fulfill steps in article.",
    )
    locals().update({"@type": Field("TechArticle", const=True)})


TechArticle.update_forward_refs()
