from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class ReplyAction(CommunicateAction):
    """The act of responding to a question/message asked/sent by the object. Related to [[AskAction]]"
     "Related actions: * [[AskAction]]: Appears generally as an origin of a ReplyAction.

    See: https://schema.org/ReplyAction
    Model depth: 5
    """
    type_: str = Field(default="ReplyAction", alias='@type', constant=True)
    resultComment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        default=None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Comment import Comment
