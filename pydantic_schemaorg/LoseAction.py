from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AchieveAction import AchieveAction


class LoseAction(AchieveAction):
    """The act of being defeated in a competitive activity.

    See: https://schema.org/LoseAction
    Model depth: 4
    """

    type_: str = Field("LoseAction", const=True, alias="@type")
    winner: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="A sub property of participant. The winner of the action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    LoseAction.update_forward_refs()
