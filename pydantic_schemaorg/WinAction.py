from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schemaorg.AchieveAction import AchieveAction


class WinAction(AchieveAction):
    """The act of achieving victory in a competitive activity.

    See https://schema.org/WinAction.

    """
    type_: str = Field("WinAction", const=True, alias='@type')
    loser: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A sub property of participant. The loser of the action.",
    )
    

WinAction.update_forward_refs()
