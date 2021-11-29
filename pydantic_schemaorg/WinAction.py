from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.AchieveAction import AchieveAction


class WinAction(AchieveAction):
    """The act of achieving victory in a competitive activity.

    See https://schema.org/WinAction.

    """

    loser: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A sub property of participant. The loser of the action.",
    )
    locals().update({"@type": Field("WinAction", const=True)})


WinAction.update_forward_refs()
