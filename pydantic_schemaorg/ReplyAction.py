from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CommunicateAction import CommunicateAction


class ReplyAction(CommunicateAction):
    """The act of responding to a question/message asked/sent by the object. Related to [[AskAction]]"
     "Related actions: * [[AskAction]]: Appears generally as an origin of a ReplyAction.

    See: https://schema.org/ReplyAction
    Model depth: 5
    """

    type_: str = Field("ReplyAction", const=True, alias="@type")
    resultComment: "Optional[Union[List[Union[Comment, str]], Union[Comment, str]]]" = Field(
        None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Comment import Comment

    ReplyAction.update_forward_refs()
