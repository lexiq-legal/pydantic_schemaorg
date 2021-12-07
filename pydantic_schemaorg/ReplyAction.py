from pydantic import Field
from pydantic_schemaorg.Comment import Comment
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class ReplyAction(CommunicateAction):
    """The act of responding to a question/message asked/sent by the object. Related to [[AskAction]]"
     "Related actions: * [[AskAction]]: Appears generally as an origin of a ReplyAction.

    See https://schema.org/ReplyAction.

    """
    type_: str = Field("ReplyAction", const=True, alias='@type')
    resultComment: Optional[Union[List[Comment], Comment]] = Field(
        None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    

ReplyAction.update_forward_refs()
