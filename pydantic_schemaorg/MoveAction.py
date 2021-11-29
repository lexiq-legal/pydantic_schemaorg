from pydantic import Field
from pydantic_schemaorg.Place import Place
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Action import Action


class MoveAction(Action):
    """The act of an agent relocating to a place. Related actions: * [[TransferAction]]: Unlike"
     "TransferAction, the subject of the move is a living Person or Organization rather than"
     "an inanimate object.

    See https://schema.org/MoveAction.

    """

    fromLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    toLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    locals().update({"@type": Field("MoveAction", const=True)})


MoveAction.update_forward_refs()
