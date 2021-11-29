from pydantic import Field
from pydantic_schemaorg.LearningResource import LearningResource


class Quiz(LearningResource):
    """Quiz: A test of knowledge, skills and abilities.

    See https://schema.org/Quiz.

    """

    locals().update({"@type": Field("Quiz", const=True)})


Quiz.update_forward_refs()
