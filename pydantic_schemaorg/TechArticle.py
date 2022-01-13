from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Article import Article


class TechArticle(Article):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting,"
     "specifications, etc.

    See: https://schema.org/TechArticle
    Model depth: 4
    """

    type_: str = Field("TechArticle", const=True, alias="@type")
    proficiencyLevel: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Proficiency needed for this content; expected values: 'Beginner', 'Expert'.",
    )
    dependencies: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Prerequisites needed to fulfill steps in article.",
    )


if TYPE_CHECKING:

    TechArticle.update_forward_refs()
