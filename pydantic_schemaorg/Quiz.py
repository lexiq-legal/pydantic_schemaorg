from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LearningResource import LearningResource


class Quiz(LearningResource):
    """Quiz: A test of knowledge, skills and abilities.

    See: https://schema.org/Quiz
    Model depth: 4
    """
    type_: str = Field("Quiz", alias='@type')
    

