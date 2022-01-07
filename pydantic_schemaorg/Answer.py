from pydantic import Field
from pydantic_schemaorg.Comment import Comment
from pydantic_schemaorg.WebContent import WebContent
from typing import List, Optional, Union


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    See https://schema.org/Answer.

    """
    type_: str = Field("Answer", const=True, alias='@type')
    answerExplanation: Optional[Union[List[Union[Comment, WebContent, str]], Union[Comment, WebContent, str]]] = Field(
        None,
        description="A step-by-step or full explanation about Answer. Can outline how this Answer was achieved"
     "or contain more broad clarification or statement about it.",
    )
    

Answer.update_forward_refs()
