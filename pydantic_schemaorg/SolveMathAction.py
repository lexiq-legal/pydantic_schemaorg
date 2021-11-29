from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Action import Action


class SolveMathAction(Action):
    """The action that takes in a math expression and directs users to a page potentially capable"
     "of solving/simplifying that expression.

    See https://schema.org/SolveMathAction.

    """

    eduQuestionType: Optional[Union[List[str], str]] = Field(
        None,
        description="For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates"
     "the format of question being given. Example: \"Multiple choice\", \"Open ended\","
     "\"Flashcard\".",
    )
    locals().update({"@type": Field("SolveMathAction", const=True)})


SolveMathAction.update_forward_refs()
