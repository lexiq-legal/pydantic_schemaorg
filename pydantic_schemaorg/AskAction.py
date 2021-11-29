from pydantic import Field
from pydantic_schemaorg.Question import Question
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class AskAction(CommunicateAction):
    """The act of posing a question / favor to someone. Related actions: * [[ReplyAction]]:"
     "Appears generally as a response to AskAction.

    See https://schema.org/AskAction.

    """

    question: Optional[Union[List[Question], Question]] = Field(
        None,
        description="A sub property of object. A question.",
    )
    locals().update({"@type": Field("AskAction", const=True)})


AskAction.update_forward_refs()
