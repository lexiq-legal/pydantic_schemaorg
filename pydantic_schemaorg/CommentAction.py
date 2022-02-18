from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CommentAction(CommunicateAction):
    """The act of generating a comment about a subject.

    See: https://schema.org/CommentAction
    Model depth: 5
    """
    type_: str = Field(default="CommentAction", alias='@type', const=True)
    resultComment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        default=None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Comment import Comment
