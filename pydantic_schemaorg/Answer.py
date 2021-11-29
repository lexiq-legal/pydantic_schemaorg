from pydantic import Field
from pydantic_schemaorg.Comment import Comment
from pydantic_schemaorg.WebContent import WebContent
from typing import Any, Union, List, Optional


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    See https://schema.org/Answer.

    """

    answerExplanation: Optional[Union[List[Union[Comment, WebContent]], Union[Comment, WebContent]]] = Field(
        None,
        description="A step-by-step or full explanation about Answer. Can outline how this Answer was achieved"
     "or contain more broad clarification or statement about it.",
    )
    locals().update({"@type": Field("Answer", const=True)})


Answer.update_forward_refs()
