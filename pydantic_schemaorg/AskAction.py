from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class AskAction(CommunicateAction):
    """The act of posing a question / favor to someone. Related actions: * [[ReplyAction]]:"
     "Appears generally as a response to AskAction.

    See: https://schema.org/AskAction
    Model depth: 5
    """
    type_: str = Field(default="AskAction", alias='@type', const=True)
    question: Optional[Union[List[Union['Question', str]], 'Question', str]] = Field(
        default=None,
        description="A sub property of object. A question.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Question import Question
