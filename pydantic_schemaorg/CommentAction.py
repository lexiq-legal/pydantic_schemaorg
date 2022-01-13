from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CommentAction(CommunicateAction):
    """The act of generating a comment about a subject.

    See: https://schema.org/CommentAction
    Model depth: 5
    """

    type_: str = Field("CommentAction", const=True, alias="@type")
    resultComment: "Optional[Union[List[Union[Comment, str]], Union[Comment, str]]]" = Field(
        None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Comment import Comment

    CommentAction.update_forward_refs()
