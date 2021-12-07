from pydantic import Field
from pydantic_schemaorg.WebContent import WebContent
from pydantic_schemaorg.Comment import Comment
from typing import Any, Optional, Union, List


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    See https://schema.org/Answer.

    """
    type_: str = Field("Answer", const=True, alias='@type')
    answerExplanation: Optional[Union[List[Union[WebContent, Comment]], Union[WebContent, Comment]]] = Field(
        None,
        description="A step-by-step or full explanation about Answer. Can outline how this Answer was achieved"
     "or contain more broad clarification or statement about it.",
    )
    

Answer.update_forward_refs()
