from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CommunicateAction import CommunicateAction


class AskAction(CommunicateAction):
    """The act of posing a question / favor to someone. Related actions: * [[ReplyAction]]:"
     "Appears generally as a response to AskAction.

    See: https://schema.org/AskAction
    Model depth: 5
    """

    type_: str = Field("AskAction", const=True, alias="@type")
    question: "Optional[Union[List[Union[Question, str]], Union[Question, str]]]" = (
        Field(
            None,
            description="A sub property of object. A question.",
        )
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Question import Question

    AskAction.update_forward_refs()
