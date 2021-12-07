from pydantic import Field
from pydantic_schemaorg.MoveAction import MoveAction


class ArriveAction(MoveAction):
    """The act of arriving at a place. An agent arrives at a destination from a fromLocation,"
     "optionally with participants.

    See https://schema.org/ArriveAction.

    """
    type_: str = Field("ArriveAction", const=True, alias='@type')
    

ArriveAction.update_forward_refs()
