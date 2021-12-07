from pydantic import Field
from pydantic_schemaorg.Comment import Comment
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CommentAction(CommunicateAction):
    """The act of generating a comment about a subject.

    See https://schema.org/CommentAction.

    """
    type_: str = Field("CommentAction", const=True, alias='@type')
    resultComment: Optional[Union[List[Comment], Comment]] = Field(
        None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    

CommentAction.update_forward_refs()
