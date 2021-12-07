from pydantic import Field
from pydantic_schemaorg.LearningResource import LearningResource


class Quiz(LearningResource):
    """Quiz: A test of knowledge, skills and abilities.

    See https://schema.org/Quiz.

    """
    type_: str = Field("Quiz", const=True, alias='@type')
    

Quiz.update_forward_refs()
