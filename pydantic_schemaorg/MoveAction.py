from pydantic import Field
from pydantic_schemaorg.Place import Place
from typing import List, Optional, Union
from pydantic_schemaorg.Action import Action


class MoveAction(Action):
    """The act of an agent relocating to a place. Related actions: * [[TransferAction]]: Unlike"
     "TransferAction, the subject of the move is a living Person or Organization rather than"
     "an inanimate object.

    See https://schema.org/MoveAction.

    """
    type_: str = Field("MoveAction", const=True, alias='@type')
    fromLocation: Optional[Union[List[Union[Place, str]], Union[Place, str]]] = Field(
        None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    toLocation: Optional[Union[List[Union[Place, str]], Union[Place, str]]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    

MoveAction.update_forward_refs()
