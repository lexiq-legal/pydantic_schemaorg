from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Action import Action


class SolveMathAction(Action):
    """The action that takes in a math expression and directs users to a page potentially capable"
     "of solving/simplifying that expression.

    See: https://schema.org/SolveMathAction
    Model depth: 3
    """

    type_: str = Field("SolveMathAction", const=True, alias="@type")
    eduQuestionType: "Optional[Union[List[str], str]]" = Field(
        None,
        description="For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates"
        'the format of question being given. Example: "Multiple choice", "Open ended",'
        '"Flashcard".',
    )


if TYPE_CHECKING:

    SolveMathAction.update_forward_refs()
