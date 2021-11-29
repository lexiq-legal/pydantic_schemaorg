from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Comment import Comment


class Question(Comment):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently"
     "Asked Questions (FAQ) document.

    See https://schema.org/Question.

    """

    eduQuestionType: Optional[Union[List[str], str]] = Field(
        None,
        description="For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates"
     "the format of question being given. Example: \"Multiple choice\", \"Open ended\","
     "\"Flashcard\".",
    )
    answerCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of answers this question has received.",
    )
    suggestedAnswer: Any = Field(
        None,
        description="An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer"
     "site.",
    )
    acceptedAnswer: Any = Field(
        None,
        description="The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites"
     "vary in their selection mechanisms, e.g. drawing on community opinion and/or the view"
     "of the Question author.",
    )
    locals().update({"@type": Field("Question", const=True)})


Question.update_forward_refs()
