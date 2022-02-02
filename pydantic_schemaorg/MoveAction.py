from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Action import Action


class MoveAction(Action):
    """The act of an agent relocating to a place. Related actions: * [[TransferAction]]: Unlike"
     "TransferAction, the subject of the move is a living Person or Organization rather than"
     "an inanimate object.

    See: https://schema.org/MoveAction
    Model depth: 3
    """
    type_: str = Field("MoveAction", alias='@type')
    fromLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    toLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Place import Place
