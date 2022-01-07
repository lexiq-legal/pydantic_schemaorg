from pydantic import Field
from typing import List, Optional, Union
from pydantic_schemaorg.Answer import Answer
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.Comment import Comment


class Question(Comment):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently"
     "Asked Questions (FAQ) document.

    See https://schema.org/Question.

    """
    type_: str = Field("Question", const=True, alias='@type')
    eduQuestionType: Optional[Union[List[str], str]] = Field(
        None,
        description="For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates"
     "the format of question being given. Example: \"Multiple choice\", \"Open ended\","
     "\"Flashcard\".",
    )
    answerCount: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The number of answers this question has received.",
    )
    suggestedAnswer: Optional[Union[List[Union[Answer, ItemList, str]], Union[Answer, ItemList, str]]] = Field(
        None,
        description="An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer"
     "site.",
    )
    acceptedAnswer: Optional[Union[List[Union[ItemList, Answer, str]], Union[ItemList, Answer, str]]] = Field(
        None,
        description="The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites"
     "vary in their selection mechanisms, e.g. drawing on community opinion and/or the view"
     "of the Question author.",
    )
    

Question.update_forward_refs()
