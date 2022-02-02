from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Comment import Comment


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    See: https://schema.org/Answer
    Model depth: 4
    """
    type_: str = Field("Answer", alias='@type')
    answerExplanation: Optional[Union[List[Union['WebContent', 'Comment', str]], 'WebContent', 'Comment', str]] = Field(
        None,
        description="A step-by-step or full explanation about Answer. Can outline how this Answer was achieved"
     "or contain more broad clarification or statement about it.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.WebContent import WebContent
    from pydantic_schemaorg.Comment import Comment
